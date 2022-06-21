# If this is non-interactive, just exit.
[ ! -t 0 ] && return

# Print the reminder.
printf "\n   %s \033[38;2;255;74;106m%s\033[0m %s\n\n\n" "Run" "staginghelp" "at any time for help using this system."