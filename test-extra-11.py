import time
import pytest
import uuid
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    # wd = webdriver.Edge()
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    # driver.get("http://localhost/litecart/admin/")
    driver.get("http://localhost/litecart/")
    driver.delete_all_cookies()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'box-campaigns')))

    driver.find_element_by_css_selector('#box-account-login table a').click()
    driver.find_element_by_css_selector('#create-account input[name="tax_id"]').send_keys('12345')
    driver.find_element_by_css_selector('#create-account input[name="company"]').send_keys('ABC')
    driver.find_element_by_css_selector('#create-account input[name="firstname"]').send_keys('Ok')
    driver.find_element_by_css_selector('#create-account input[name="lastname"]').send_keys("Okk")
    driver.find_element_by_css_selector('#create-account input[name="address1"]').send_keys("Moscow Shabolovka 37")
    driver.find_element_by_css_selector('#create-account input[name="address2"]').send_keys("Moscow Shabolovka 38")
    driver.find_element_by_css_selector('#create-account input[name="postcode"]').send_keys("54321")
    driver.find_element_by_css_selector('#create-account input[name="city"]').send_keys("San Francisco")
    box = driver.find_elements_by_css_selector('#create-account select[name="country_code"] option')
    for elem in box:
        if elem.text == 'United States':
            elem.click()
            break

    time.sleep(2)
    box = driver.find_elements_by_css_selector('#create-account select[name="zone_code"] option')
    for elem in box:
        if elem.text == 'California':
            elem.click()
            break
    mail = str(uuid.uuid4()) + '@mail.ru'
    driver.find_element_by_css_selector('#create-account input[name="email"]').send_keys(mail)


    time.sleep(5)
















