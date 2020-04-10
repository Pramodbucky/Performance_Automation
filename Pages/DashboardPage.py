import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Sky_Geek_Selenium_UnitTest.locators.Locators import Locators

class dashboardpageclass():
    def __init__(self, driver):
        self.driver = driver
        self.vendorname_dropdown_xpath = "//*[@id='select2-vendorName-container']"
        self.vendorname_toenter_xpath = "/html/body/span/span/span[1]/input"
        self.vendorname_searchresult_xpath = "//*[@id='select2-vendorName-results']/li"
        self.search_button_xpath = "//*[@id='SearchText']"
        self.warning_dialog_xpath = "//*[@id='BackgroundCatalogModal']"
        self.warningno_button_xpath = "//*[@id='btnNoBackgroundCatalogModalModal']"

    def click_search_type(self,search_option):
        self.driver.find_element_by_css_selector(Locators.advance_search_xpath).click()

    def click_vendor_name(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.vendor_name)))

            vendor_name = self.driver.find_element(By.XPATH, Locators.vendor_name)
            vendor_name.click()

        except TimeoutException:
            print('Timeout vendor_name')

    def add_vendor_name(self, vendor_name):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.vendor_name_input)))

            vendor_name_input = self.driver.find_element_by_xpath(Locators.vendor_name_input)
            vendor_name_input.send_keys(vendor_name)
            time.sleep(5)
            vendor_name_input.send_keys(Keys.ENTER)

        except TimeoutException:
            print('Timeout Vendor_name')

    def click_search_button(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Locators.search_text)))
            search_button = self.driver.find_element(By.XPATH, Locators.search_text)
            search_button.click()

        except TimeoutException:
            print('Timeout Search_Failed')

    def wait_for_search_result(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.table_row)))

        except TimeoutException:
            print('Timeout table_row')

    def click_bulk_item(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.element_to_be_clickable((By.XPATH, Locators.bulk_item)))
            bulk_item = self.driver.find_element(By.XPATH, Locators.bulk_item)
            bulk_item.click()
        except TimeoutException:
            print('Timeout wait_bulk_vendor_save')

    def click_bulk_item_load_all(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.element_to_be_clickable((By.XPATH, Locators.bulk_item_load_all)))
            bulk_item_load_all = self.driver.find_element(By.XPATH, Locators.bulk_item_load_all)
            bulk_item_load_all.click()
        except TimeoutException:
            print('Timeout bulk_item_load_all')

    def wait_bulk_item_update(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_item_update_wait)))
        except TimeoutException:
            print('Timeout bulk_item_update')

    def bulk_vendor_product(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Locators.bulk_vendor)))
            bulk_vendor = self.driver.find_element(By.XPATH, Locators.bulk_vendor)
            bulk_vendor.click()
            print('bulk vendor clicked')

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_vendor_dropdown)))
            bulk_vendor_dropdown = self.driver.find_element(By.XPATH, Locators.bulk_vendor_dropdown)
            li = bulk_vendor_dropdown.find_elements(By.TAG_NAME, 'li')
            li[1].click()

        except TimeoutException:
            print('Timeout bulk_vendor')

    def wait_bulk_vendor(self):

        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_vendor_table_row)))

        except TimeoutException:
            print('Timeout bulk_vendor_table_row')

    def save_bulk_vendor(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_vendor_save)))
            bulk_vendor_save = self.driver.find_element(By.XPATH, Locators.bulk_vendor_save)
            bulk_vendor_save.click()

        except TimeoutException:
            print('Timeout save_bulk_vendor')

    def wait_bulk_vendor_save(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_vendor_successful)))
        except TimeoutException:
            print('Timeout wait_bulk_vendor_save')

    def set_search_text(self, search_text):
        try:
            text_search_input = self.driver.find_element(By.XPATH, Locators.full_text_search)
            text_search_input.clear()
            text_search_input.send_keys(search_text)

        except TimeoutException as e:
            return 'Setting Text error'

    def switch_criteria(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, Locators.is_exactly)))
            store_selector = Select(self.driver.find_element(By.XPATH, Locators.is_exactly))
            store_selector.select_by_visible_text('Begins With')

        except TimeoutException:
            print('Timeout is_exactly')

    def click_first_product(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, Locators.search_result_first_product)))
            product = self.driver.find_element(By.XPATH, Locators.search_result_first_product)
            product.click()

        except TimeoutException:
            print('Product not loaded')

    def set_product_category_from(self):
        try:

            product_category_from = self.driver.find_element(By.XPATH, Locators.product_category_from)
            self.driver.execute_script("arguments[0].scrollIntoView();", product_category_from)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.product_category_from))
            )
            product_category_from.click()

            product_category_from_input = self.driver.find_element(By.XPATH, Locators.product_category_from_input)
            product_category_from_input.send_keys(75)
            time.sleep(2)
            product_category_from_input.send_keys(Keys.ENTER)

        except TimeoutException:
            print('Timeout product_category_from')

    def set_product_category_to(self):
        try:
            product_category_to = self.driver.find_element(By.XPATH, Locators.product_category_to)
            self.driver.execute_script("arguments[0].scrollIntoView();", product_category_to)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Locators.product_category_to))
            )
            product_category_to.click()

            product_category_to_input = self.driver.find_element(By.XPATH, Locators.product_category_to_input)
            product_category_to_input.send_keys(75)
            time.sleep(2)
            product_category_to_input.send_keys(Keys.ENTER)

        except TimeoutException:
            print('Timeout product_category_from')