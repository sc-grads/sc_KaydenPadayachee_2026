/* =========================

   CREATE DATABASE

========================= */

IF DB_ID('Timesheet_ETL') IS NULL

BEGIN

    CREATE DATABASE Timesheet_ETL;

END

GO
 
USE Timesheet_ETL;

GO
 
/* =========================

   EMPLOYEE TABLE

========================= */

IF OBJECT_ID('dbo.Employee', 'U') IS NULL

BEGIN

    CREATE TABLE dbo.Employee (

        EmployeeID INT IDENTITY(1,1) PRIMARY KEY,

        FullName NVARCHAR(100),

        Email NVARCHAR(100)

    );

END

GO
 
/* =========================

   PROJECT TABLE

========================= */

IF OBJECT_ID('dbo.Project', 'U') IS NULL

BEGIN

    CREATE TABLE dbo.Project (

        ProjectID INT IDENTITY(1,1) PRIMARY KEY,

        ProjectName NVARCHAR(100)

    );

END

GO
 
/* =========================

   STAGING TABLE

========================= */

IF OBJECT_ID('dbo.Staging_Timesheet', 'U') IS NULL

BEGIN

    CREATE TABLE dbo.Staging_Timesheet (

        StagingID INT IDENTITY(1,1) PRIMARY KEY,

        WorkDate NVARCHAR(50),

        DayOfWeek NVARCHAR(20),

        ClientName NVARCHAR(100),

        ClientProjectName NVARCHAR(200),

        Description NVARCHAR(500),

        BillableStatus NVARCHAR(50),

        Comments NVARCHAR(MAX),

        TotalHours NVARCHAR(250),

        StartTime TIME,

        EndTime TIME,

        SourceFile NVARCHAR(255),

        LoadDate DATETIME DEFAULT GETDATE()

    );

END

GO
 
/* =========================

   TIMESHEET TABLE

========================= */

IF OBJECT_ID('dbo.Timesheet', 'U') IS NULL

BEGIN

    CREATE TABLE dbo.Timesheet (

        TimesheetID INT IDENTITY(1,1) PRIMARY KEY,

        EmployeeID INT,

        ProjectID INT,

        WorkDate DATE,

        StartTime TIME,

        EndTime TIME,

        HoursWorked DECIMAL(5,2),
 
        FOREIGN KEY (EmployeeID) REFERENCES dbo.Employee(EmployeeID),

        FOREIGN KEY (ProjectID) REFERENCES dbo.Project(ProjectID)

    );

END

GO
 
/* =========================

   AUDIT TABLE

========================= */

IF OBJECT_ID('dbo.ETL_AuditLog', 'U') IS NULL

BEGIN

    CREATE TABLE dbo.ETL_AuditLog (

        AuditID INT IDENTITY(1,1) PRIMARY KEY,

        FileName NVARCHAR(255),

        TableName NVARCHAR(100),

        OperationType NVARCHAR(50),

        RecordCount INT,

        Status NVARCHAR(50),

        ErrorMessage NVARCHAR(MAX),

        LogDate DATETIME DEFAULT GETDATE()

    );

END

GO
 