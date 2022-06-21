# install_profile_scripts role
This role copies several scripts to /etc/profile.d. These scripts are run automatically when any user logs in.

## colordmesg.sh
This script creates an alias so that `dmesg` is always run with -L for colorized output.

## colorip.sh
This script creates an alias so that `ip` is always run with -c for colorized output.

## commvaultps1.sh
This script creates the PS1 environment variable that defines the standard shell prompt.

## history.sh
This script creates environment variables that define how bash history behaves:
* HISTIGNORE is a list of patterns for which matching commands should not be added to history. 
* HISTCONTROL=ignoreboth prevents duplicate commands from being kept, and commands that start with a space.