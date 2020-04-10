import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
from Config import Config
from Tests.utilities.timer import Timer
from Tests.utilities.reporter import Reporter
from Pages.DashboardPage import dashboardpageclass
from Pages.ProductPage import productpageclass
from Pages.LoginPage import loginpageclass
from Pages.LogoutPage import logoutclass


class simplesearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=Config.CHROME_WEBDRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Simple_Search(self):
        driver = self.driver

        timer = Timer()
        reporter = Reporter()

        start = timer.get_time()
        reporter.append_row('Simple Search Test', start, start, start, '--')
        reporter.report()

        run_time = timer.get_time()

        driver.get("http://192.168.1.25:8081/Datahub")
        Login = loginpageclass(driver)
        Login.set_username(Config.SKY_GEEK_LOGIN_USERNAME)
        Login.set_password(Config.SKY_GEEK_LOGIN_PASSWORD)
        Login.submit()

        DashboardSearch = dashboardpageclass(driver)
        DashboardSearch.set_search_text('ewq')
        DashboardSearch.switch_criteria()

        time.sleep(10)

        DashboardSearch.click_search_button()
        start = timer.get_time()
        DashboardSearch.wait_for_search_result()
        end = timer.get_time()

        duration = timer.get_elapsed(start, end)

        reporter.append_row('Catalog Search', start, run_time, duration, 'Loading')

        time.sleep(2)

        start = timer.get_time()
        DashboardSearch.click_first_product()
        end = timer.get_time()

        duration = timer.get_elapsed(start, end)
        reporter.append_row('Product Load', start, run_time, duration, 'Loading')

        ProductPageChange = productpageclass(driver)
        ProductPageChange.append_name()
        ProductPageChange.expand_all_tab()
        ProductPageChange.update_product_fields()
        ProductPageChange.click_pricing_vendor_tab()
        ProductPageChange.update_product_cost()

        ProductPageChange.save_product()
        ProductPageChange.save_product_popup()

        # ProductPageChange.wait_for_loading()
        start = timer.get_time()
        total_duration = ProductPageChange.product_save_success_message()

        reporter.append_row('Save Product Fields', start, run_time, total_duration, 'Loading')


        reporter.report()


    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.close()
        cls.driver.quit()
        # pass
