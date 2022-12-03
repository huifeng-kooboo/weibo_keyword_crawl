# python 通过浏览器方式获取cookie
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import by
import time
web_browser = webdriver.Safari()
web_browser.get("https://weibo.com/login.php")
time.sleep(10)
print("执行点击操作")
el_button = web_browser.find_element_by_a("xx")
ActionChains(web_browser).move_to_element(el_button).click()
ActionChains(web_browser).click()
time.sleep(10)
print("END")
