
Select * from [dbo].[Employee]

Select * from[dbo].[Sales]

SELECT * FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpName = s.EmpName

SELECT * FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]

SELECT e.EmpID,e.EmpName,s.SalesNumber,s.ItemSold FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
order by e.EmpID

SELECT count(s.SalesNumber),e.EmpID,e.EmpName FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
group by e.EmpID,e.EmpName

SELECT count(s.SalesNumber) AS NoOfSales,e.EmpID,e.EmpName FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
group by e.EmpID,e.EmpName