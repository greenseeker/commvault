# If this is non-interactive, just exit.
[ ! -t 0 ] && return

# Create the aliases.
alias http='http --session $$'
alias https='https --session $$'