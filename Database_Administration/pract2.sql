      CREATE TABLE SQLBackupRestoreTest (
        ID INT NOT NULL PRIMARY KEY,
        loginname VARCHAR(100) NOT NULL,
        logindate DATETIME NOT NULL DEFAULT getdate()

        )
      GO 

    select * from SQLBackupRestoreTest

      insert into SQLBackupRestoreTest (ID,loginname) values (1,'test1')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (2,'test2')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (3,'test3')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (4,'test4')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (5,'test5')


      
      -- FULL Back up 5 rows


      insert into SQLBackupRestoreTest (ID,loginname) values (6,'test6')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (7,'test7')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (8,'test8')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (9,'test9')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (10,'test10')



    -- diff back up 10 rows 



      insert into SQLBackupRestoreTest (ID,loginname) values (11,'test11')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (12,'test12')
      
      insert into SQLBackupRestoreTest (ID,loginname) values (13,'test13')



      -- tran log back -1 up 13 rows 

      insert into SQLBackupRestoreTest (ID,loginname) values (14, 'test14')

      insert into SQLBackupRestoreTest (ID,loginname) values (15, 'test15')

      insert into SQLBackupRestoreTest (ID,loginname) values (16, 'test16')

      insert into SQLBackupRestoreTest (ID,loginname) values (17, 'test17')

 --FULL AND DIFF

      -- tran log back - 2 up 17 rows 



      insert into SQLBackupRestoreTest (ID,loginname) values (114, 'test114')
      -- Jul 26 2021 7:17AM

      --Jul 26 2021  7:26AM
      insert into SQLBackupRestoreTest (ID,loginname) values (115, 'test115')
      
     

      --Jul 26 2021 7:27AM

      insert into SQLBackupRestoreTest (ID,loginname) values (116, 'test116')

      insert into SQLBackupRestoreTest (ID,loginname) values (117, 'test117')

      --


      print getdate()
      --Jul 26 2021 7:17AM




      USE [master]
      RESTORE DATABASE [AdventureWorks2016] FROM DISK = N'C:\SQL_BACKUPS\AdventureWorks2016_full.BAK' WITH FILE = 1, NORECOVERY, NOUNLOAD, STATS = 5

      GO 


      USE [master]
      RESTORE DATABASE [AdventureWorks2016] FROM DISK = N'C:\SQL_BACKUPS\AdventureWorks2016_dife_1.diff' WITH FILE = 1, NORECOVERY, NOUNLOAD, STATS = 5

      GO 

       RESTORE LOG [AdventureWorks2016] FROM DISK = N'C:\SQL_BACKUPS\AdventureWorks2016_tran_3.trn' WITH FILE = 1, NORECOVERY, NOUNLOAD, STATS = 10
       GO 



      RESTORE DATABASE AdventureWorks2016 WITH RECOVERY 
      GO 



      RESTORE DATABASE [AdventureWorks2016_RestoreTest] WITH RECOVERY 
      GO
