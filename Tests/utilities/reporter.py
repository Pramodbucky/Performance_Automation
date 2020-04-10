import pandas as pd
from datetime import datetime


class Reporter:
    def __init__(self):
        self.log_path = 'C://Users//pkc//Desktop//Pramod//Sky_Geek_Selenium_UnitTest//Sky_Geek_Selenium_UnitTest//log//'
        self.file_name = 'sky_geek_report_' + datetime.now().strftime("%b_%d_%Y ")
        self.full_path = self.log_path + self.file_name + '.csv'

        try:
            df = pd.read_csv(self.full_path, dtype=object, encoding='ISO-8859-1').fillna('')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['process', 'date', 'time', 'duration', 'tag'])

        self.df = df

    def append_row(self, process, date, time, duration, tag):
        print('Writing ' + process)
        temp_df = pd.DataFrame()
        temp_df['process'] = [process]
        temp_df['date'] = [date.strftime("%m/%d/%Y")]
        temp_df['time'] = [time.strftime("%H:00")]
        temp_df['duration'] = [duration]
        temp_df['tag'] = [tag]

        self.df = self.df.append(temp_df)

    def append_row_job(self, process, date, time, duration, tag):
        print('Writing ' + process)
        temp_df = pd.DataFrame()
        temp_df['process'] = [process]
        temp_df['date'] = [date.strftime("%m/%d/%Y")]
        temp_df['time'] = [time]
        temp_df['duration'] = [duration]
        temp_df['tag'] = [tag]

        self.df = self.df.append(temp_df)

    def report(self):
         self.df.to_csv(self.full_path, index=False)
