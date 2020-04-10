import logging


class Logger:
    log_path = "C://Users//pkc//Desktop//Pramod//Sky_Geek_Selenium_UnitTest//Sky_Geek_Selenium_UnitTest//log//logs.log'"
    logging.basicConfig(filename=log_path, format='%(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')

    @staticmethod
    def add_log(log):
        logging.info(log)

    @staticmethod
    def add_error(error):
        logging.error(error)
