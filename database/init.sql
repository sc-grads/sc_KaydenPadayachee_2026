-- Create database Cloud-tunnel-JP
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'Cloud-tunnel-KP')
BEGIN
    EXECUTE('CREATE DATABASE [Cloud-tunnel-JP]');
    PRINT 'Database [Cloud-tunnel-KP] created successfully';
END
GO
 
USE [Cloud-tunnel-KP];
GO
 
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'People')
BEGIN
    CREATE TABLE People (
        PersonID INT IDENTITY(1,1) PRIMARY KEY,
        FirstName NVARCHAR(50) NOT NULL,
        LastName NVARCHAR(50) NOT NULL,
        CreatedDate DATETIME DEFAULT GETDATE()
    );
    PRINT 'People table created successfully';
END
GO
INSERT INTO People (FirstName, LastName) VALUES 
('Jabulane', 'Poulo'),
('Thabo', 'Nkosi'),
('Lerato', 'Mbeki'),
('Sipho', 'Dlamini'),
('Nomsa', 'Zulu'),
('Alice', 'Johnson'),
('Bob', 'Smith'),
('Carol', 'Davis'),
('David', 'Wilson'),
('Eve', 'Brown');
 
GO
SELECT PersonID, FirstName, LastName, CreatedDate FROM People;
GO
 
PRINT 'Deployment completed successfully';