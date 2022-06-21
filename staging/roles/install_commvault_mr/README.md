# install_commvault_mr role

The Feature Release number is used with the get_mr.sql.j2 template to create /run/staging/get_mr.sql.

The SQL script is executed with sqlcmd to fetch the Maintenance Release which was installed in the customer's environment.

The matching Maintenance Release is then installed from /mnt/cvupdates.