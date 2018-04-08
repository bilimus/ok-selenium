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

    box = driver.find_elements_by_css_selector('#box-apps-menu a')
    for i in range(16):
        print(box[i].text)
        box[i].click()
        box = driver.find_elements_by_css_selector('#box-apps-menu a')
        for j in range(len(box) - 16):
            print(box[i+j+1].text)
            box[i+j+1].click()
            box = driver.find_elements_by_css_selector('#box-apps-menu a')
            time.sleep(0.2)
        time.sleep(0.2)

