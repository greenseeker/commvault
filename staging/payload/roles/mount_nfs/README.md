# mount_nfs role

This role makes sure mount.nfs is installed, then mounts the escalationlogs, CVUpdates, and CVMedia shares from eng, and the CloudUploads share from titan, all under under /mnt. These mounts are attempted using NFSv3 first for better throughput, then fallback to NFSv4 in case of failure.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`