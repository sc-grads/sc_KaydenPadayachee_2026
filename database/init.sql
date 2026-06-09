-- Create database if it doesn't exist
IF DB_ID('DBCLOUDTUNNELINGKP') IS NULL
BEGIN
    CREATE DATABASE DBCLOUDTUNNELINGKP;
END
GO
 
-- Switch to database
USE DBCLOUDTUNNELINGKP;
GO
 
-- Create Users table if it doesn't exist
IF OBJECT_ID('Users', 'U') IS NULL
BEGIN
    CREATE TABLE Users (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Name NVARCHAR(100),
        Email NVARCHAR(100) UNIQUE
    );
END
GO
 
-- Seed data (no duplicates)
IF NOT EXISTS (SELECT 1 FROM Users WHERE Email = 'alice@test.com')
INSERT INTO Users (Name, Email) VALUES ('Alice', 'alice@test.com');
 
IF NOT EXISTS (SELECT 1 FROM Users WHERE Email = 'bob@test.com')
INSERT INTO Users (Name, Email) VALUES ('Bob', 'bob@test.com');
 
IF NOT EXISTS (SELECT 1 FROM Users WHERE Email = 'charlie@test.com')
INSERT INTO Users (Name, Email) VALUES ('Charlie', 'charlie@test.com');
GO