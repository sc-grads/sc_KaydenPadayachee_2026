BACKUP DATABASE [FileGroupDemoDatabase] FILEGROUP = N'FG_2020',  FILEGROUP = N'FG_2019' TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\Backup\FileGroupDemoDatabase.bak' 
WITH NOFORMAT, NOINIT,  NAME = N'FileGroupDemoDatabase-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO
