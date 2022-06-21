#!/usr/bin/env python3

from os import execl
from os.path import isfile
import distro
from socket import getfqdn, gethostbyname
from pathlib import Path
import re

dist = f"{distro.name()} {distro.version()}"
tz = Path('/etc/localtime').resolve().as_posix().strip("/usr/share/zoneinfo")
host = getfqdn().lower()
ip = gethostbyname(host)
pw = f"cv_{host.split('.')[0]}"

try:
    with open ("/etc/CommVaultRegistry/Galaxy/Instance001/.properties","r") as prop:
        reg = prop.readlines()

    with open ("/etc/CommVaultRegistry/Galaxy/Instance001/UpdateBinTransactions/.properties") as prop:
        reg += prop.readlines()

    r = re.compile("^sProductVersion [0-9.]")
    try:
        major = list(filter(r.match, reg))[0].strip("sProductVersion ").split('.')[0]
    except:
        major = "?"

    r = re.compile("^SPTranID")
    try:
        feature = re.sub(r"SPTranID\s+SP","",list(filter(r.match, reg))[0]).split("_")[0]
    except IndexError:
        feature = 0
    except:
        feature = "?"

    r = re.compile("^UP_Transaction")
    try:
        maint = re.sub(r"UP_Transaction\s+","",list(filter(r.match, reg))[0]).split('_')[0]
    except IndexError:
        maint = 0
    except:
        maint = "?"

    version = f"{major}.{feature}.{maint}"
    if "?" in f"{major}.{feature}.{maint}": version = version

except FileNotFoundError:
    version = "?"

if isfile("/etc/gotty/banner_template.ans"):
    with open("/etc/gotty/banner_template.ans","r") as banfile:
        banner = banfile.read()
elif isfile("banner_template.ans"):
    with open("banner_template.ans","r") as banfile:
        banner = banfile.read()
else:
    pass

banner = banner.replace("@@HOSTNAME@@", host, 1)
banner = banner.replace("@@IPADDR@@", ip, 1)
banner = banner.replace("@@VERSION@@", version, 1)
banner = banner.replace("@@DISTRO@@", dist, 1)
banner = banner.replace("@@TZ@@", tz, 1)
banner = banner.replace("@@PASSWORD@@", pw, 1)

print(banner)

user = input(f"login [root]: ")
if user == "": user = "root"

execl(f"/usr/bin/ssh","-o UserKnownHostsFile=/dev/null","-o StrictHostKeyChecking=no","-o LogLevel=ERROR",f"{user}@{host.split('.')[0]}")
