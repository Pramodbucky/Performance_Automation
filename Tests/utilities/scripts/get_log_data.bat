@echo off

sqlcmd.exe -U dh_admin -P Summer@2014 -S 192.168.1.26 -Q"EXECUTE msdb..sp_help_jobhistory @job_name='GenerateSeomBackSynFile'" -o "G:\log_Generate.csv" -W -w 1024 -s","

sqlcmd.exe -U dh_admin -P Summer@2014 -S 192.168.1.26 -Q"EXECUTE msdb..sp_help_jobhistory @job_name='ScanSeomFileForBackSyncIntoUDH'" -o "G:\log_ScanSeom.csv" -W -w 1024 -s","
