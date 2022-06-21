# install_json_tools role

This role installs command line tools for working with json:
* jid - json incremental digger
* jq - json query


jid is not available in any repo, so the binary is included. It also includes a profile script to define an alias for jid.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`