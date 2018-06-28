from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get('http://abcollect.service.dev.africanbank.net/')

assert "Login" in driver.title

elem = driver.find_element_by_id("id_username")
elem.send_keys('root')

elem = driver.find_element_by_id("id_password")
elem.send_keys('verysecret')

elem.send_keys(Keys.RETURN)

driver = webdriver.Firefox()
driver.get("http://abcollect.service.dev.africanbank.net/")
assert "Python" in driver.title

elem = driver.find_element_by_id("id_username")
elem.send_keys('root')

elem = driver.find_element_by_id("id_password")
elem.send_keys('verysecret')

elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()
'''