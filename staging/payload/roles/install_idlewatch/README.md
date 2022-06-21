# install_idletools role

This role installs the idlewatch scripts and service, which is used on the staging backend to get system idle time for the purpose of suspending the VM.

This role also creates /etc/profile.d/bashtimeout.sh which configures TMOUT at login to terminate idle user sessions.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`