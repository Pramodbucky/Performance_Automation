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
from Pages.BulkItemUpdatePage import bulkitemupdateclass
from Tests.utilities.timer import Timer
from Tests.utilities.reporter import Reporter

class BulkItemTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=Config.CHROME_WEBDRIVER)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_bulkitem(self):
        driver = self.driver

        timer = Timer()
        reporter = Reporter()

        start = timer.get_time()
        reporter.append_row('Bulk Item Update Test', start, start, start, '--')
        reporter.report()

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
        DashboardSearch.wait_for_search_result()

        time.sleep(4)

        DashboardSearch.click_bulk_item()
        DashboardSearch.click_bulk_item_load_all()

        start = timer.get_time()
        DashboardSearch.wait_bulk_item_update()
        end = timer.get_time()

        duration = timer.get_elapsed(start, end)

        reporter.append_row('Bulk Item Update Table Data Load', start, end, duration, 'Loading')
        reporter.report()

        bulkitemupdate = bulkitemupdateclass(driver)
        bulkitemupdate.bulk_item_update_choose()
        bulkitemupdate.bulk_item_update_choose_fill_input('made-in-usa')
        bulkitemupdate.bulk_item_update_add_to_grid()
        bulkitemupdate.wait_bulk_item_update_ht_auto_complete()
        bulkitemupdate.change_bulk_item_update_table()

        
        start = bulkitemupdate.save_bulk_item_update()
        end = timer.get_time()

        duration = timer.get_elapsed(start, end)

        reporter.append_row('Bulk Item Update Saving', start, end, duration, 'Loading')
        reporter.report()

        Logout = logoutclass(driver)
        Logout.click_logout()


    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.close()
        cls.driver.quit()
        # pass