select BusinessEntityID,firstname,lastname
into #TempPersonTable
from [Person].[Person]
where title = 'mr.'

DROP TABLE #TempPersonTable
Create table #TempPersonTable (
BussinessEntityID int,
Firstname nvarchar (50),
lastanem nvarchar(50),
TITLE nvarchar (50)
)

INSERT INTO #TempPersonTable
SELECT BusinessEntityID,Firstname,lastName,Title
from [Person].[Person]
where title = 'mr.'

SELECT *FROM #TempPersonTable;