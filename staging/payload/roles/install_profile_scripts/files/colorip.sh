# If this is non-interactive, just exit.
[ ! -t 0 ] && return

# Create the alias
alias ip='ip -c'