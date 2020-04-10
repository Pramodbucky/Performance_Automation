from selenium.webdriver.support.ui import WebDriverWait
from locators.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from Tests.utilities.logger import Logger
import Config.Database as dbConn

class loginpageclass():
    def __init__(self,driver):
        self.driver = driver

    def get_logo(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.logo)))
            Logger.add_log('Logo present')
            return 'Logo Present'
        except TimeoutException as e:
            Logger.add_error('Logo not found ' + str(e))
            return 'Logo not found'

    def get_tag_line(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.tag_line)))
            Logger.add_log('Tag present')
            return 'Tag Present'
        except TimeoutException as e:
            Logger.add_error('Tag not found ' + str(e))
            return 'Tag not found'

    def get_version(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.version)))
            version = self.driver.find_element(By.XPATH, Locators.version)
            Logger.add_log('Version ' + version.text)
            return version.text
        except TimeoutException as e:
            Logger.add_error('Version not found ' + str(e))
            return 'Version not found'

    def get_username(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.username)))
            Logger.add_log('Username input found')
            return 'Username input found'
        except TimeoutException as e:
            Logger.add_error('Username input not found ' + str(e))
            return 'Username input not found'

    def get_password(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.password)))
            Logger.add_log('Password input found')
            return 'Password input found'
        except TimeoutException as e:
            Logger.add_error('Password input not found ' + str(e))
            return 'Password input not found'

    def get_submit(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.login)))
            Logger.add_log('Login button found')
            return 'Login button found'
        except TimeoutException as e:
            Logger.add_error('Login button not found ' + str(e))
            return 'Login button not found'

    def set_username(self, username):
        try:
            username_input = self.driver.find_element(By.XPATH, Locators.username)
            username_input.clear()
            username_input.send_keys(username)
            Logger.add_log('Username set')
        except TimeoutException as e:
            Logger.add_error('Setting username error ' + str(e))
            return 'Setting username error'

    def set_password(self, password):
        try:
            password_input = self.driver.find_element(By.XPATH, Locators.password)
            password_input.clear()
            password_input.send_keys(password)
            Logger.add_log('Password set')
        except TimeoutException as e:
            Logger.add_error('Setting password error ' + str(e))
            return 'Setting password error'

    def submit(self):
        try:
            login = self.driver.find_element(By.XPATH, Locators.login)
            login.click()

        except TimeoutException as e:
            Logger.add_error('Login failed ' + str(e))
            return 'Login failed'