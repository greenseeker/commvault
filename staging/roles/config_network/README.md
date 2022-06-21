# config_network role

This role applies configuration to the NIC, updates /etc/hosts, fixes the hostname, regenerates the ssh host keys, and registers with DNS.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`