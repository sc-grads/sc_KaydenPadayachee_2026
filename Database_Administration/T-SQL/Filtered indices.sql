CREATE NONCLUSTERED INDEX idx_tblEmployee_Employee  
    ON dbo.tblEmployee(EmployeeNumber) where EmployeeNumber<139;
--the rest of the script is under nonclustered