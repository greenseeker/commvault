#!/usr/bin/env python3

from yaml import dump as yamldump, safe_load as yamlread
from sys import argv
from os import makedirs, environ, system as exec
from re import sub

def main():
    args = argv[1:]                                       # Everything after the script name is an argument

    proxy_url = "http://172.19.240.161:9888"              # The HTTP(S) proxy to access the outside world
    environ['http_proxy'] = proxy_url
    environ['https_proxy'] = proxy_url

    # Build a dictionary from the command line arguments
    parameters = {}
    parameters['test_mode'] = False                       # Default value to avoid a key error later if it's not set
    parameters['ansible_vers'] = '4.9.0'                  # Default value to avoid a key error later if it's not set

    for item in args:
        key = item.split('=')[0]
        value = item.split('=')[1]

        if value.lower() == "true": value = True          # Convert text true/false to proper boolean
        elif value.lower() == "false": value = False

        parameters[key]=value

    with open('/etc/staging/repo.yaml','r') as repofile:
        repo_dict = yamlread(repofile)

    payload_url = repo_dict['main']

    script_log = '/var/log/staging/initiator.log'
    staging_temp = '/run/staging'

    makedirs('/var/log/staging',exist_ok=True)

    with open(script_log,"w") as logfile:
        if parameters['test_mode']:                       # If test_mode is true, use the test branch...
            logfile.write("!!--- RUNNING IN TEST MODE ---!!\n")
            branch = 'test'
        else:                                             # ...otherwise the main branch.
            branch = 'main'

        logfile.write(f"Creating {staging_temp}... ")     # create directories
        try:
            makedirs(staging_temp,mode=0o700,exist_ok=True)
            logfile.write("SUCCESS.\n")
        except:
            logfile.write("FAILURE.\n")
        
        try:
            logfile.write(f"Parameters: {parameters}.\n")
            logfile.write(f"Writing parameters to {staging_temp}/parameters.yaml... ")
            with open (f"{staging_temp}/parameters.yaml", "w") as pfile:
                pfile.write("---\n")
                yamldump(parameters, pfile)               # write parameters to a yaml file for the ansible playbook to read
                yamldump({"proxy_url": proxy_url}, pfile) # keeping this separate from parameters prevents it from being logged
            logfile.write("SUCCESS.\n")
        except:
            logfile.write("FAILURE.\n")

        try:
            logfile.write(f"Updating pip3 to the latest... ")
            exec(f"/usr/bin/python3 -m pip install -U pip")
            logfile.write(f"SUCCESS.\n")
        except:
            logfile.write(f"FAILURE.\n")

        try:
            logfile.write(f"Installing Ansible {parameters['ansible_vers']} via pip3... ")
            exec(f"/usr/local/bin/pip3 install -U ansible=={parameters['ansible_vers']}")
            logfile.write("SUCCESS.\n")
        except:
            logfile.write("FAILURE.\n")

        try:
            # payload_url manipulation in the next line is to prevent the credentials from being logged
            logfile.write(f"Executing site.yaml playbook from the {branch} branch of {sub('//.+@','//',payload_url)}. See /var/log/staging/ansible.log for details... ")
            exec(f"/usr/bin/env ansible-pull --purge --checkout {branch} --url {payload_url} site.yaml")       # run the ansible playbook
            logfile.write("SUCCESS.\n")
        except:
            logfile.write("FAILURE.\n")

if __name__ == '__main__':
    main()

# eof