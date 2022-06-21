# install_knockd role

This role installs the knockd (knock-server) service. This is used to monitor communications related to Command Center, Web Console, Commcell Console, SSMS, etc, for the purposes of tracking idle time for VM suspend.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`