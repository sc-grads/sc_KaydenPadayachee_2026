

select * from[Sales].[vSalesPerson]

drop table salesstaff 

select * from SalesStaff





 select * from sales.vSalesPerson

 

 drop table salesstaff

 
select firstname + ' ' + Lastname AS Fullname,
[TerritoryName],
[TerritoryGroup],
[SalesQuota],
[SalesYTD],[SalesLastYear]
 into salesstaff
 from sales.vSalesPerson



select * from salesstaff



update salesstaff set [SalesQuota] = 500000.00



update salesstaff set [SalesQuota] = SalesQuota + 1500000.00



update salesstaff set [SalesQuota] = SalesQuota + 1500000.00 , SalesYTD =  SalesYTD - 500,SalesLastYear = SalesLastYear * 1.5



update salesstaff set [TerritoryName] = 'UK' where [TerritoryName] = 'United Kingdom'




update salesstaff set [TerritoryName] = 'UK' where [TerritoryGroup] is null and fullname = 'syed Abbas'



update salesstaff set TerritoryName = 'UK', TerritoryGroup = 'Europe' where TerritoryGroup is null and fullname = 'syed Abbas'



update salesstaff set SalesQuota = sp.salesquota
from salesstaff ss
inner join sales.vSalesPerson sp
on ss.Fullname = (sp.firstname + ' ' + sp.lastname)
