CREATE FUNCTION fnc_TransactionTotal (@intEmployee as int)
returns money
as
begin
declare @TotalAmount as money
select @TotalAmount = sum(Amount) 
from [dbo].[tblTransaction]
where EmployeeNumber = @intEmployee
return @TotalAmount
end

set showplan_all on
go
set showplan_text on
go
select [EmployeeNumber], dbo.fnc_TransactionTotal([EmployeeNumber]) 
from [dbo].[tblEmployee]

select E.[EmployeeNumber], sum(Amount) as TotalAmount
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.[EmployeeNumber]
set statistics time off
set showplan_all off

select EmployeeNumber, dbo.fnc_TransactionTotal(EmployeeNumber)
from dbo.tblEmployee

select E.EmployeeNumber, sum(T.Amount) as TotalAmount
from dbo.tblEmployee as E
left join dbo.tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber

select E.EmployeeNumber, (select sum(Amount) from tblTransaction as T 
                          where T.EmployeeNumber = E.EmployeeNumber) as TotalAmount
from dbo.tblEmployee as E
