UPDATE umusers SET enabled = 1 WHERE (id = 1 OR login = 'admin' OR login = 'cvadmin' OR login = 'ROMS')