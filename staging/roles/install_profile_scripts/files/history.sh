# If this is non-interactive, just exit.
[ ! -t 0 ] && return

# Create the variables.
export HISTIGNORE=*http_proxy*:*https_proxy*
export HISTCONTROL=ignoreboth