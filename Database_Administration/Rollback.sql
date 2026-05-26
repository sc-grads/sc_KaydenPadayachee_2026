DBCC CHECKDB	('AdventureWorks2016')
DBCC CHECKDB    ('AdventureWorks2016') with no_infomsgs

alter database AdventureWorks2016 set single_user with rollback immediate
go
dbcc checkdb ('AdventureWorks2016',REPAIR_ALLOW_DATA_LOSS)
GO
alter database AdventureWorks2016 set MULTI_user with rollback immediate
GO
