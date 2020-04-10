from selenium.webdriver.support.ui import WebDriverWait
from Sky_Geek_Selenium_UnitTest.locators.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class logoutclass():
    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        try:
            logout_button = self.driver.find_element(By.XPATH, Locators.logout)
            logout_button.click()

        except TimeoutException as e:
            return 'Logout failed'