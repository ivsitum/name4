from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

action = ActionChains(browser)
browser.find_element_by_xpath("//*[contains(text(),'Meher')]").click()
automation.delay()
source = browser.find_element_by_css_selector(".wrapper>ul>li:last-child")
action.move_to_element(source).perform()
browser.find_element_by_css_selector(".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(2)").click()
browser.find_element_by_xpath("//input[@name='name']").click()
browser.find_element_by_xpath("//input[@name='name']").send_keys("Smiley")
automation.delay()
browser.find_element_by_xpath("//*[@data-emoji='smiley']").click()
automation.delay()
browser.close()
