@echo off
setlocal enabledelayedexpansion

sqlcmd.exe -U dh_admin -P Summer@2014 -S 192.168.1.26 -Q"EXECUTE msdb.dbo.sp_start_job @job_name='GenerateSeomBackSynFile'"

sqlcmd.exe -U dh_admin -P Summer@2014 -S 192.168.1.26 -Q"EXECUTE msdb.dbo.sp_start_job @job_name='ScanSeomFileForBackSyncIntoUDH'"


