select * from [dbo].[Student] 

select * from [dbo].[Course] 



select * from [dbo].[Student] s
inner join [dbo].[Course] c 
on s.RollNo = c.RollNO


select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
inner join [dbo].[Course] c 
on s.RollNo = c.RollNO


select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
join [dbo].[Course] c 
on s.RollNo = c.RollNO


select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
left join [dbo].[Course] c 
on s.RollNo = c.RollNO



select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
right join [dbo].[Course] c 
on s.RollNo = c.RollNO


select s.RollNo,s.StudentName,c.CourseID from [dbo].[Student] s
full join [dbo].[Course] c 
on s.RollNo = c.RollNO