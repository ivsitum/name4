from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.SearchPage import SearchPage
import time
import os
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class LoginPage(BasePage):
    """Object Repository"""

    EMAIL = (By.XPATH, "//input[@id='emailOrUsername']")
    PASSWORD = (By.XPATH, "//input[@id='pass']")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(text(),'Login')]")

    AVATAR = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]")
    LOGOUT_BUTTON = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='My Account'])[1]/following::span[2]")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(data.url)

    """Page Actions"""
    """this is used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to login"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(3)
        return SearchPage(self.driver)

    def do_logout(self):
        self.do_click(self.AVATAR)
        time.sleep(2)
        self.do_click(self.LOGOUT_BUTTON)

    def is_logout_successful(self):
        return self.is_visible(self.EMAIL)





