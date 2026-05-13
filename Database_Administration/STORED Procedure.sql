
CREATE PROCEDURE [dbo].[SelectAllPersonAddress]
AS
SELECT * FROM  Person.Address
go;

SELECT * from Person.Address



exec [dbo].[SelectAllPersonAddress]

drop procedure SelectAllPersonAddress

drop procedure [dbo].[SelectAllPersonAddressWithParams]

Create Procedure SelectAllPersonAddressWithParams (@City NVARCHAR (30))
AS

SET NOCOUNT ON

Select * from Person.Address where City =@city;

END


exec SelectAllPersonAddressWithParams @city = 'New York'


exec SelectAllPersonAddressWithParams 'Miami'


drop procedure [SelectAllPersonAddressWithParams]


CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParams] (@City NVARCHAR(30) = 'New York')
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO



exec SelectAllPersonAddressWithParams 'Miami'

exec SelectAllPersonAddressWithParams @city = 'Miami'



CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParams] (@City NVARCHAR(30) = 'New York',@stateProvinceid int)
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO



CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParamswithEncryption] (@City NVARCHAR(30) = 'New York',@stateProvinceid int)
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END
GO

CREATE PROCEDURE [dbo].[SelectAllPersonAddressWithParamswithEncryption] (@City NVARCHAR(30) = 'New York')
WITH ENCRYPTION
AS

BEGIN
SET NOCOUNT ON

SELECT * FROM  Person.Address where City = @city;

END