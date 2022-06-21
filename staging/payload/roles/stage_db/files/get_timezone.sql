set nocount on
use commserv
SELECT TZ.TimeZoneStdName from SchedTimeZone TZ JOIN APP_ClientProp CP on CP.attrVal = TZ.TimeZoneID WHERE CP.attrName = 'timezone Id'