-- char - ASCII - 1 byte
-- varchar - ASCII - 1 byte
-- nchar - UNICODE - 2 bytes
-- nvarchar - UNICODE - 2 bytes

-- ASCII: A-Z, a-z, 0-9  
--       65   97   48   32  128 
-- (0-255)

DECLARE @chrMyCharacters as char(10)

-- DECLARE @chrMyCharacters as varchar(10)  still takes 2 bytes in storage

set @chrMyCharacters = 'hello'

SELECT @chrMyCharacters as myString, len(@chrMyCharacters) as MyLength, DATALENGTH(@chrMyCharacters) as MyDataLength

-- Always prefix nchar and nvarchar values with N (capital N).

go


DECLARE @chrMyCharacters as nvarchar(10)

-- DECLARE @chrMyCharacters as varchar(10)  still takes 2 bytes in storage

set @chrMyCharacters = N'hello'

SELECT @chrMyCharacters as myString, len(@chrMyCharacters) as MyLength, DATALENGTH(@chrMyCharacters) as MyDataLength

-- Always prefix nchar and nvarchar values with N (capital N).