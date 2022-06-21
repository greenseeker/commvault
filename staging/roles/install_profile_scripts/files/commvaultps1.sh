# If this is non-interactive, just exit.
[ ! -t 0 ] && return

# Use one value for root, or another for anyone else.
if [ $(id -u) == 0 ]
then
    export PS1='\[\e[48;2;11;46;68m\]\[\e[38;2;255;74;106m\]\u@\h \[\e[38;2;221;229;237m\]\w \[\e[38;2;255;74;106m\]\$\[\e[m\] '
else
    export PS1='\[\e[48;2;11;46;68m\]\[\e[38;2;221;229;237m\]\u@\h \w \$\[\e[m\] '
fi