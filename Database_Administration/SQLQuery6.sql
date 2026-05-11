CREATE TABLE [dbo].[salesstaff](
	[staffid] [int] NOT NULL PRIMARY KEY,
	[fName] [nvarchar](30) NOT NULL,
	[lName] [nvarchar](30) NOT NULL
	)

	insert into salesstaff (staffid,fname,lname) VALUES (200,'kayden','padayachee')


	select * from salesstaff


	insert into salesstaff (staffid,fname,lname) VALUES (300,'hailey','naicker'),(325,'john','vick'),(314,'james','dino')

	
CREATE TABLE [dbo].[salesstaffNew](
	ID [int] not null IDENTITY PRIMARY KEY,
	[staffid] [int] NOT NULL,
	[fName] [nvarchar](30),
	[lName] [nvarchar](30)
	)

	SELECT * FROM salesstaffNew

insert into salesstaffNew (staffid,fname,lname) VALUES (200,'kayden','padayachee')


insert into salesstaffNew (staffid,fname,lname) VALUES (300,'hailey','naicker'),(325,'john','vick'),(314,'james','dino')

	



CREATE TABLE [dbo].[nameOnlyTable](
	
	[fName] [nvarchar](30),
	[lName] [nvarchar](30)
	)


select * from nameOnlyTable

insert into nameOnlyTable (fname,lname)
select fname,lname from salesstaffNew where id >= 3

select * into salesstaffNew_bkp from salesstaffNew --bkp is backup

