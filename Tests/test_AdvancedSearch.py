import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver

from Config import Config
from Pages.LoginPage import loginpageclass
from Pages.LogoutPage import logoutclass
from Pages.DashboardPage import dashboardpageclass
from Tests.utilities.timer import Timer
from Tests.utilities.reporter import Reporter


class AdvancedSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=Config.CHROME_WEBDRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_advance_search(self):
        driver = self.driver

        timer = Timer()
        reporter = Reporter()

        start = timer.get_time()
        reporter.append_row('Bulk Vendor Product Test', start, start, start, '--')
        reporter.report()

        run_time = timer.get_time()

        driver.get("http://192.168.1.25:8081/Datahub")
        Login = loginpageclass(driver)
        Login.set_username(Config.SKY_GEEK_LOGIN_USERNAME)
        Login.set_password(Config.SKY_GEEK_LOGIN_PASSWORD)
        Login.submit()

        DashboardSearch = dashboardpageclass(driver)
        #       1->Simple 2->Advanced 3->BulkPricing 4->BulkItem
        DashboardSearch.click_search_type(2)
        DashboardSearch.click_vendor_name()
        DashboardSearch.add_vendor_name("M. Eagles Tool Warehouse Inc")
        DashboardSearch.set_product_category_from()
        DashboardSearch.set_product_category_to()
        time.sleep(2)

        DashboardSearch.click_search_button()
        start = timer.get_time()
        DashboardSearch.wait_for_search_result()
        end = timer.get_time()
        duration = timer.get_elapsed(start, end)

        # reporter.append_row('Advanced Search(BVP)', start, run_time, duration, 'Loading')

        time.sleep(2)

        DashboardSearch.bulk_vendor_product()
        start = timer.get_time()
        DashboardSearch.wait_bulk_vendor()
        end = timer.get_time()
        duration = timer.get_elapsed(start, end)

        reporter.append_row('Advanced Search', start, run_time, duration, 'Loading')

        DashboardSearch.save_bulk_vendor()
        start = timer.get_time()
        DashboardSearch.wait_bulk_vendor_save()
        end = timer.get_time()
        duration = timer.get_elapsed(start, end)

        reporter.append_row('Bulk Item Save', start, run_time, duration, 'Saving')
        reporter.report()

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
