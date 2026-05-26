BACKUP DATABASE [AdventureWorks2016] TO  DISK = N'C:\SQLBackup\AdventureWork2016_diff_1.diff' WITH  DIFFERENTIAL ,
NOFORMAT, NOINIT,  NAME = N'AdventureWorks2016-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO
