import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from locators.Locators import Locators
from Tests.utilities.timer import Timer

class bulkitemupdateclass():
    def __init__(self, driver):
        self.driver = driver
        self.timer = Timer()

    def bulk_item_update_choose(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.choose_field)))
            choose_field = self.driver.find_element(By.XPATH, Locators.choose_field)
            choose_field.click()
        except TimeoutException:
            print('Timeout bulk_item_update')

    def bulk_item_update_choose_fill_input(self, _input):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.choose_field_input)))
            choose_field_input = self.driver.find_element(By.XPATH, Locators.choose_field_input)
            choose_field_input.send_keys(_input)
            time.sleep(2)
            choose_field_input.send_keys(Keys.ENTER)
        except TimeoutException:
            print('Timeout bulk_item_update_choose_fill_input')

    def bulk_item_update_add_to_grid(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.add_to_grid)))
            add_to_grid = self.driver.find_element(By.XPATH, Locators.add_to_grid)
            add_to_grid.click()
        except TimeoutException:
            print('Timeout bulk_item_update_add_to_grid')

    def wait_bulk_item_update_ht_auto_complete(self):
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.invisibility_of_element_located((By.XPATH, Locators.loading_message)))

        except TimeoutException:
            print('Timeout wait_bulk_item_update_ht_auto_complete')

    def change_bulk_item_update_table(self):
        try:
            WebDriverWait(self.driver, 300).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_item_update_table)))

            bulk_item_update_table_id = self.driver.find_element_by_xpath(Locators.bulk_item_update_table)
            bulk_item_update_column_data = bulk_item_update_table_id.find_elements_by_xpath("//tr/td[" + str(2) + "]")
            celltext = []
            for column in bulk_item_update_column_data:
                celltext.append(column.text)
            celltext = list(filter(None, celltext))

            WebDriverWait(self.driver, 300).until(
                EC.visibility_of_element_located((By.XPATH, Locators.bulk_item_update_made_in_usa_dropdown)))

            self.bulk_item_update(celltext)

        except TimeoutException:
            print('Timeout Bulk_Item_Update_Table')

    def bulk_item_update(self,celltext):
        made_in_usa_first_column = self.driver.find_element_by_xpath(Locators.bulk_item_update_made_in_usa_dropdown)
        made_in_usa_first_column.click()
        if "Yes" in celltext[0]:
            self.driver.find_element_by_xpath('//td[.="No"]').click()
            time.sleep(3)
        else:
            self.driver.find_element_by_xpath('//td[.="Yes"]').click()
            time.sleep(3)
        made_in_usa_context_click = self.driver.find_element_by_xpath(Locators.bulk_item_update_second_column)
        actions = ActionChains(self.driver)
        actions.context_click(made_in_usa_context_click).perform()
        click_table_id = self.driver.find_element_by_xpath(Locators.bulk_item_update_right_click_table)
        list_rows = click_table_id.find_elements_by_tag_name("tr")
        list_rows[0].click()

    def save_bulk_item_update(self):
        timer = self.timer
        try:
            WebDriverWait(self.driver, 3000).until(
                EC.invisibility_of_element_located((By.XPATH, Locators.loading_message)))

            save_bulk_item_update = self.driver.find_element(By.XPATH, Locators.save_bulk_item_update)
            save_bulk_item_update.click()
            start = timer.get_time()

            WebDriverWait(self.driver, 3000).until(
                EC.visibility_of_element_located((By.XPATH, Locators.success_message)))

            return start

        except TimeoutException:
            print('Timeout wait_bulk_item_update_ht_auto_complete')


