# install_gotty role

This role installs the web-based terminal application, Gotty (https://github.com/yudai/gotty).

Gotty binary, config file, and service definition are included.

Also included are banner_template.ans and login.py which are used to present an info screen and login prompt when a user connects to Gotty, and login.html which customizes the page where Gotty is embedded. distro.py is the Python distro module used by login.py.

The role also opens port 8080 for Gotty's use, then starts and enables the new Gotty service.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`