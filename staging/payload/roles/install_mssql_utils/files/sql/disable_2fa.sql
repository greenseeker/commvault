UPDATE GXGlobalParam SET value = 0, modified = (SELECT DATEDIFF(s, '1970-01-01 00:00:00', GETUTCDATE())) WHERE name='EnableTwoFactorAuthentication'