select*
from [dbo].[tblEmployee]
join [dbo].[tblTransaction]
on [dbo].[tblEmployee]. EmployeeNumber - tblTransaction.EmployeeNumber