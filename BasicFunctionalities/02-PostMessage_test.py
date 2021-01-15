from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit

automation = AutomationInit()
browser = automation.getBrowser()
automation.login()

def test_InPrivateChannel():
    browser.find_element_by_xpath("//*[contains(text(),'rocketchat-qa')]").click()
    browser.find_element_by_xpath("//*[@name='msg']").click()
    browser.find_element_by_xpath("//*[@name='msg']").send_keys("Hello testing")
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)

def test_InPublicChannel():
    automation.delay()
    browser.find_element_by_xpath("//*[contains(text(),'sandbox')]").click()
    automation.delay(2)
    browser.find_element_by_xpath("//*[@name='msg']").click()
    browser.find_element_by_xpath("//*[@name='msg']").send_keys("Hello testing")
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
    automation.delay()
    browser.close()




