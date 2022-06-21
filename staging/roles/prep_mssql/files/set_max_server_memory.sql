use master
exec sp_configure 'show advanced options', 1
reconfigure
exec sp_configure 'max server memory', 10240    -- Limit the instance to 10GB RAM
reconfigure