# prep_mssql role

This role copies set_max_server_memory.sql to /run/staging and creates /run/staging/change_sa_password.sql from the change_sa_password.sql.j2 template. These scripts are then executed with sqlcmd to set the SQL Server instance memory limit and to reset the sa password to cv_*hostname*.