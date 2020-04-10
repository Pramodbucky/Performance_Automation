import time
from datetime import datetime


# noinspection PyMethodMayBeStatic
class Timer:
    def get_time(self):
        _date = datetime.now()
        return _date

    def get_elapsed(self, start, end):
        difference = end - start
        return difference.total_seconds()
