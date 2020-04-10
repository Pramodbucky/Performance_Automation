import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Sky_Geek_Selenium_UnitTest.Tests.utilities.timer import Timer
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from Sky_Geek_Selenium_UnitTest.locators.Locators import Locators

class productpageclass():
    def __init__(self, driver):
        self.driver = driver
        self.timer = Timer()
        self.start = self.timer.get_time()
        self.end = self.timer.get_time()
        self.duration = self.timer.get_time()

    def append_name(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.product_name)))

            vendor_name = self.driver.find_element(By.XPATH, Locators.product_name)
            vendor_name.send_keys('-')

        except TimeoutException:
            print('Product name not located')

    def expand_all_tab(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.expand_all_tab)))

            vendor_name = self.driver.find_element(By.XPATH, Locators.expand_all_tab)
            vendor_name.click()

        except TimeoutException:
            print('Expand Tab not found')


    def update_product_fields(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.altspec_airbus_pn)))
            altspec_tab = self.driver.find_element(By.XPATH, Locators.altspec_airbus_pn)
            altspec_tab.send_keys('-')

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.altspec_manufacture_pn)))
            altspec_tab = self.driver.find_element(By.XPATH, Locators.altspec_manufacture_pn)
            altspec_tab.send_keys('-')

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.item_technical_materials)))
            altspec_tab = self.driver.find_element(By.XPATH, Locators.item_technical_materials)
            altspec_tab.send_keys('-')

        except TimeoutException:
            print('Timeout update_product_fields')

    def click_pricing_vendor_tab(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.pricing_vendor)))

            pricing_vendor = self.driver.find_element(By.XPATH, Locators.pricing_vendor)
            self.driver.execute_script("window.scrollTo(0, 0);")
            pricing_vendor.click()

        except TimeoutException:
            print('Pricing Tab not found')

    def update_product_cost(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.product_cost)))

            product_cost = self.driver.find_element(By.XPATH, Locators.product_cost)
            cost = int(float(product_cost.get_attribute('value')))
            cost -= 1
            time.sleep(2)
            product_cost.clear()
            product_cost.send_keys(cost)

        except TimeoutException:
            print('Timeout update cost')

    def save_product(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.save_product_cost)))
            save_product_cost = self.driver.find_element(By.XPATH, Locators.save_product_cost)
            save_product_cost.click()

        except TimeoutException:
            print('Timeout update_fields')

    def save_product_popup(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.save_product_warning_window)))
            time.sleep(3)
            save_product_cost = self.driver.find_element(By.XPATH, Locators.save_product_warning_window_yes)
            save_product_cost.click()

        except TimeoutException:
            print('Timeout save_product Warning Window')

    def product_save_success_message(self):
        try:

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.success_message)))
            success_message = self.driver.find_element(By.XPATH, Locators.success_message)

            while success_message.get_attribute("class") != 'alert alert-success':
                print('Waiting')
                print('old start time {}'.format(self.start))
                self.start = self.timer.get_time()
                hello = self.start
                print('new start time {}'.format(hello))
        except TimeoutException:
            print('Timeout save_wait_product')
        except StaleElementReferenceException:
            print('old end time {}'.format(self.end))
            self.end = self.timer.get_time()
            print('new end time {}'.format(self.end))

        return self.timer.get_elapsed(hello, self.end)

    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located((By.XPATH, Locators.product_cost)))
            print('Hello')

        except TimeoutException:
            print('Timeout save_product_reload')

        except StaleElementReferenceException:
            print("Wait ended")