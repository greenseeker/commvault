# install_httpie role

This role installs HTTPie from PyPI, then creates /etc/profile.d/httpie.sh which creates aliases for the `http` and `https` commands when users log in.

This role also places some json files in /root/rest which can be used with httpie.