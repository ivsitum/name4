from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
automation.delay(2)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").click()
automation.delay(2)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys("Meher")
automation.delay()
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(Keys.ENTER)
automation.delay()
browser.find_element_by_xpath("//*[@name='msg']").click()
browser.find_element_by_xpath("//span[@class='rc-message-box__icon emoji-picker-icon js-emoji-picker']").click()
browser.find_element_by_xpath("//input[@name='name']").click()
browser.find_element_by_xpath("//input[@name='name']").send_keys("Smiley")
automation.delay()
browser.find_element_by_xpath("//*[@data-emoji='smiley']").click()
automation.delay()
browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
automation.delay()

automation.logout()
automation.delay()
browser.close()

