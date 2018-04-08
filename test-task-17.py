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

    driver.find_element_by_css_selector('#box-apps-menu a[href*="catalog"]').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                                    'form[name="catalog_form"] a[href*="category_id=1"]')))
    driver.find_element_by_css_selector('form[name="catalog_form"] a[href*="category_id=1"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                                    '#content a[href*="product_id"]')))
    #time.sleep(1)
    box = driver.find_elements_by_css_selector('#content a[href*="product_id"]')
    len_box = len(box)

    for i in range(0, len_box, 2):

        box[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                                        'button[name="save"]')))
        #time.sleep(1)
        driver.find_element_by_css_selector('#box-apps-menu a[href*="catalog"]').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                           'form[name="catalog_form"] a[href*="category_id=1"]')))
        #time.sleep(1)
        driver.find_element_by_css_selector('form[name="catalog_form"] a[href*="category_id=1"]').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, \
                                                                        '#content a[href*="product_id"]')))
        box = driver.find_elements_by_css_selector('#content a[href*="product_id"]')
        #time.sleep(1)
    for l in driver.get_log("browser"):
        assert (len(l) == 0) is True
    time.sleep(2)
