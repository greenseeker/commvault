# install_mssql_utils role

This role installs mssql-utils and mssql-cli, and then creates /etc/profile.d/mssqlcli.sh to set up the MSSQL* environment variables at user login.

A collection of sql files are copied to /root/sql for user convenience when manually restoring the DB.

Make sure the per-distro task files follow the "{{ ansible_distribution|lower }}{{ ansible_distribution_major_version }}.yaml" format. The following command can be run on a system to see how Ansible reports the relevant values: `ansible localhost -m setup | grep -E 'ansible_distribution\b|ansible_distribution_major_version\b'`