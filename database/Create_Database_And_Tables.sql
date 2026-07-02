-- ==========================================
-- 1. DATABASE SETUP
-- ==========================================
 
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'TimesheetDB1')
BEGIN
    CREATE DATABASE TimesheetDB1;
END;
GO
 
USE TimesheetDB1;
GO
 
-- ==========================================
-- 2. AUDIT LOG TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.AuditLog', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.AuditLog
    (
        AuditID INT IDENTITY(1,1)
            CONSTRAINT PK_AuditLog PRIMARY KEY,
 
        PackageName NVARCHAR(100) NOT NULL
            CONSTRAINT DF_AuditLog_Pkg
            DEFAULT 'GraduateTimesheet_ETL',
 
        TaskName NVARCHAR(100) NOT NULL
            CONSTRAINT DF_AuditLog_Task
            DEFAULT 'Clean and Normalize Core Tables',
 
        FileName NVARCHAR(260) NULL,
 
        RowsStaged INT NOT NULL
            CONSTRAINT DF_AuditLog_Staged DEFAULT 0,
 
        InsertsProcessed INT NOT NULL
            CONSTRAINT DF_AuditLog_Inserts DEFAULT 0,
 
        UpdatesProcessed INT NOT NULL
            CONSTRAINT DF_AuditLog_Updates DEFAULT 0,
 
        DeletesProcessed INT NOT NULL
            CONSTRAINT DF_AuditLog_Deletes DEFAULT 0,
 
        LeaveRowsProcessed INT NOT NULL
            CONSTRAINT DF_AuditLog_Leave DEFAULT 0,
 
        Status NVARCHAR(20) NOT NULL,
 
        [Message] NVARCHAR(MAX) NULL,
 
        LogTimestamp DATETIME
            CONSTRAINT DF_AuditLog_Time DEFAULT GETDATE(),
 
        ExecutedBy NVARCHAR(100) NOT NULL
            CONSTRAINT DF_AuditLog_User DEFAULT SYSTEM_USER
    );
 
    ALTER TABLE dbo.AuditLog
    ADD CONSTRAINT CK_AuditLog_Status
    CHECK (Status IN ('Running','Success','Failed'));
END;
GO
 
-- ==========================================
-- 3. CLIENT TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.Client', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Client
    (
        ClientID INT IDENTITY(1,1)
            CONSTRAINT PK_Client PRIMARY KEY,
 
        ClientName VARCHAR(200) NOT NULL
    );
END;
GO
 
-- ==========================================
-- 4. EMPLOYEE TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.Employee', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Employee
    (
        EmployeeID INT IDENTITY(1,1)
            CONSTRAINT PK_Employee PRIMARY KEY,
 
        FirstName NVARCHAR(150) NOT NULL,
        LastName NVARCHAR(150) NULL
    );
END;
GO
 
-- ==========================================
-- 5. LEAVE TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.Leave', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Leave
    (
        LeaveID INT IDENTITY(1,1)
            CONSTRAINT PK_Leave PRIMARY KEY,
 
        EmployeeID INT NULL
            CONSTRAINT FK_Leave_Employee
            FOREIGN KEY REFERENCES dbo.Employee(EmployeeID),
 
        LeaveDate DATE NULL,
        LeaveType NVARCHAR(250) NOT NULL
    );
END;
GO
 
-- ==========================================
-- 6. STAGING TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.StagingTimesheet', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.StagingTimesheet
    (
        StagingID INT IDENTITY(1,1)
            CONSTRAINT PK_StagingTimesheet PRIMARY KEY,
 
        EmployeeSourceFile NVARCHAR(MAX),
        RawDate NVARCHAR(50),
        RawDayOfWeek NVARCHAR(50),
        RawClient NVARCHAR(150),
        RawProjectName NVARCHAR(150),
        RawDescription NVARCHAR(MAX),
        RawBillableStatus NVARCHAR(50),
        RawComments NVARCHAR(MAX),
        RawTotalHours NVARCHAR(50),
        RawStartTime NVARCHAR(50),
        RawEndTime NVARCHAR(50),
        EmployeeName NVARCHAR(MAX)
    );
END;
GO
 
-- ==========================================
-- 7. TIMESHEET TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.Timesheet', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Timesheet
    (
        TimesheetID INT IDENTITY(1,1)
            CONSTRAINT PK_Timesheet PRIMARY KEY,
 
        EmployeeID INT NULL
            CONSTRAINT FK_Timesheet_Employee
            FOREIGN KEY REFERENCES dbo.Employee(EmployeeID),
 
        ClientID INT NULL
            CONSTRAINT FK_Timesheet_Client
            FOREIGN KEY REFERENCES dbo.Client(ClientID),
 
        WorkDate DATE NULL,
 
        DayOfWeek NVARCHAR(50) NULL,
 
        BillableStatus NVARCHAR(50) NULL,
 
        StartTime TIME NULL,
 
        EndTime TIME NULL,
 
        TotalHours NVARCHAR(50) NULL,
 
        TaskDescription NVARCHAR(MAX) NULL,
 
        Comments NVARCHAR(MAX) NULL,
 
        LastUpdatedDate DATETIME
            CONSTRAINT DF_Timesheet_LastUpdate
            DEFAULT GETDATE()
    );
END;
GO
 
-- ==========================================
-- 8. CLEAR STAGING TABLE
-- ==========================================
 
IF OBJECT_ID('dbo.StagingTimesheet', 'U') IS NOT NULL
BEGIN
    TRUNCATE TABLE dbo.StagingTimesheet;
END;
GO
 
PRINT 'TimesheetDB1 database and tables verified successfully.';
GO