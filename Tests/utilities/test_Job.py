import subprocess
import pandas as pd
from datetime import datetime
import time
from Tests.utilities.reporter import Reporter
from Tests.utilities.timer import Timer

subprocess.call([r'C:\Users\pkc\Desktop\Pramod\Sky_Geek_Selenium_UnitTest\Sky_Geek_Selenium_UnitTest\Tests\utilities\scripts\check_jobs.bat'])

time.sleep(120)

subprocess.call([r'C:\Users\pkc\Desktop\Pramod\Sky_Geek_Selenium_UnitTest\Sky_Geek_Selenium_UnitTest\Tests\utilities\scripts\get_log_data.bat'])

time.sleep(5)


reporter = Reporter()
timer = Timer()
start = timer.get_time()

def readfile(filename):
    df = pd.read_csv(filename)
    second_row = df.iloc[1]
    run_duration = second_row['run_duration']
    run_time = second_row['run_time']

    if len(run_time)>5:
        run_time = second_row['run_time'][:2] + ":" + second_row['run_time'][2:4] + ":" + second_row['run_time'][4:]
    else:
        run_time = second_row['run_time'][0] + ":" + second_row['run_time'][1:3] + ":" + second_row['run_time'][3:]

    if len(run_duration) > 2:
        run_duration = second_row['run_duration'][0] + " minutes " + second_row['run_duration'][1:] + " seconds "
    else:
        run_duration = second_row['run_duration'][:] + " seconds "

    print("Runtime of job {} started on {} date on time {} is {}".format(second_row['job_name'], second_row['run_date'], second_row['run_time'], run_duration))

    reporter.append_row_job('Job Time Calculation', start, run_time, run_duration, 'Running')
    reporter.report()

readfile("G:\log_Generate.csv")
readfile("G:\log_ScanSeom.csv")