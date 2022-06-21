#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps as dumpjson
from os.path import getmtime
from time import time as now
from urllib.parse import urlparse

"""
This script runs a simple HTTP server that returns a JSON object containing
idleMins for the purpose of querying the VM's idle time to determine when it
should be suspended. If URL parameter debug = true, then details for each 
knockd-monitored service are returned as well.
"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_params = { 'debug': 'false' }   # default URL params
        knockd_log_commands = []            # blank this list
        ssh_last_triggered = False          # *_last_triggered variables start as False
        gotty_last_triggered = False
        mailhog_last_triggered = False
        http_last_triggered = False
        https_last_triggered = False
        sqlserver_last_triggered = False
        evmgrs_last_triggered = False

        # Get URL parameters, if any, and use them to update url_params dict.
        param_query = urlparse(self.path).query
        if param_query: url_params['debug'] = dict(component.split("=") for component in param_query.split("&"))['debug']

        # Set last_activity to the number of minutes since .LASTACTIVITY mtime 
        # or 0 if .LASTACTIVITY doesn't exist.
        try:
            idle_mins = int((now() - getmtime('/var/log/staging/.LASTACTIVITY')) / 60)
        except FileNotFoundError:
            idle_mins = 0
        
        # Send HTTP response and headers
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        # If debug=true, read the knockd.log and get the latest update for each
        # service.
        if url_params['debug'] == 'true':
            with open('/var/log/staging/knockd.log') as fileobj:
                knockd_log = fileobj.readlines()
            knockd_log_commands = [line.strip() for line in knockd_log if 'running command' in line]

            for x in range(len(knockd_log_commands) - 1, 0, -1):
                if ' ssh: ' in knockd_log_commands[x] and not ssh_last_triggered:
                    ssh_last_triggered = knockd_log_commands[x]
                elif ' gotty: ' in knockd_log_commands[x] and not gotty_last_triggered:
                    gotty_last_triggered = knockd_log_commands[x]
                elif ' MailHog: ' in knockd_log_commands[x] and not mailhog_last_triggered:
                    mailhog_last_triggered = knockd_log_commands[x]
                elif ' http: ' in knockd_log_commands[x] and not http_last_triggered:
                    http_last_triggered = knockd_log_commands[x]
                elif ' https: ' in knockd_log_commands[x] and not https_last_triggered:
                    https_last_triggered = knockd_log_commands[x]
                elif ' sqlserver: ' in knockd_log_commands[x] and not sqlserver_last_triggered:
                    sqlserver_last_triggered = knockd_log_commands[x]
                elif ' EvMgrS: ' in knockd_log_commands[x] and not evmgrs_last_triggered:
                    evmgrs_last_triggered = knockd_log_commands[x]
                elif ssh_last_triggered and gotty_last_triggered and mailhog_last_triggered and http_last_triggered and https_last_triggered and sqlserver_last_triggered and evmgrs_last_triggered:
                    break

            self.wfile.write(dumpjson({                # Send HTTP body in JSON
                'idleMins': idle_mins,
                '_sshLastActivity': ssh_last_triggered,
                '_gottyLastActivity': gotty_last_triggered,
                '_mailhogLastActivity': mailhog_last_triggered,
                '_httpLastActivity': http_last_triggered,
                '_httpsLastActivity': https_last_triggered,
                '_sqlserverLastActivity': sqlserver_last_triggered,
                '_evmgrsLastActivity': evmgrs_last_triggered
            }).encode())
        else:
            self.wfile.write(dumpjson({                # Send HTTP body in JSON
                'idleMins': idle_mins,
            }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 32000), RequestHandler)
    server.serve_forever()