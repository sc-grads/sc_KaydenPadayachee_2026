CREATE NONCLUSTERED INDEX [IDX_FIRSTNAME] ON [Person].[Person]
(
	[FirstName] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)

GO

CREATE NONCLUSTERED INDEX [idx_firstname_lastname] ON [Person].[Person]
(
	[FirstName] ASC
)
INCLUDE ( 	[LastName]) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)

GO


dbcc checkdb ('AdventureWorks2016')



dbcc checkdb ('AdventureWorks2016') with no_infomsgs



alter database AdventureWorks2016 set single_user with rollback immediate
go
dbcc checkdb ('AdventureWorks2016', REPAIR_ALLOW_DATA_LOSS)
GO
alter database AdventureWorks2016 set MULTI_user with rollback immediate
go




SELECT COUNT(*) FROM [Person].[Person]



ALTER TABLE [Person].[Person] ADD  CONSTRAINT [PK_Person_BusinessEntityID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO


