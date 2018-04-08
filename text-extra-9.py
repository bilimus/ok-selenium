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

def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False

def test_example(driver):
    # driver.maximize_window()
    driver.get("http://localhost/litecart/admin/")
    driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-apps-menu")))

    driver.find_element_by_css_selector('#box-apps-menu a[href*="countries"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content a")))
    box = driver.find_elements_by_css_selector('#content a')
    for i in range(4, len(box), 2):
       assert (box[i-2].text < box[i].text) is True

    box = driver.find_elements_by_css_selector('#content td')

    for i in range(5, len(box), 7):
        if box[i].text != '0':
            box[i-1].find_element_by_css_selector('a').click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content button[name="save"]')))
            box = driver.find_elements_by_css_selector('#table-zones td')
            for j in range(6, len(box)-3, 4):
                assert (box[j - 4].text < box[j].text) is True
            driver.find_element_by_css_selector('#box-apps-menu a[href*="countries"]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content td")))
            box = driver.find_elements_by_css_selector('#content td')
            # time.sleep(10)