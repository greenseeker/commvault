# stage_db role

Starts SQL Server.

Converts database_path UNC path to /mnt/escalationlogs (NFS) path.

If a database dump has been provided, run restore_db.yaml tasks.
* The DB is restored using CSRecoveryAssistant.sh.
* If CSRA fails due to binary mismatch, run install_commvault_mr role to apply Maintenance Release, then rerun CSRA.
* The customer's time zone is pulled from that database using get_timezone.sql.

If this is "NODB", the nodb.yaml tasks are executed.
* Put the DB in staging mode with CSRA.
* Update the CS hostname with SetpreImagedNames.

csdb_changes.sql is created from template then run with sqlcmd to update a variety of settings within the CSDB; see that file for specifics.

The staging server's time zone is set to the time zone from above. If no time zone was determined (because of NODB or failure), the time zone is set to Etc/UTC.

Updates OEM.properties and galaxy.jnlp with appropriate values.