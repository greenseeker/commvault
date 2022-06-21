This script is used for manual log collection on the following Unix platforms:
* AIX
* FreeBSD
* HPUX
* Linux
* macOS
* Solaris

Commonly used for systems which are not communicating and therefore logs can't be collected via Commvault's built-in function.

In addition to Commvault's Log_Files directory, /etc/CommVaultRegistry, and other files, this script will also collect a substantial amount of system information (system log, network/firewall config, kernel parameters, installed packages, etc). It can also optionally collect information about certain databases.

After making the script executable (`chmod +x uxLogs.sh`) you can run `./uxLogs --help` to see usage. Run `./uxLogs` as root to collect the logs.
