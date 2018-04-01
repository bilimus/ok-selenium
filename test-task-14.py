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
    WebDriverWait(driver, 10).until(\
        EC.presence_of_element_located((By.CSS_SELECTOR, '#content a[href*="edit_country"]')))

    driver.find_element_by_css_selector('#content a[href*="edit_country"]').click()
    WebDriverWait(driver, 10).until(\
        EC.presence_of_element_located((By.CSS_SELECTOR, '#content')))
    time.sleep(2)
    box = driver.find_elements_by_css_selector('#content table a[href^="http"]')
    for elem in box:
        first_window = driver.current_window_handle
        win_handles = driver.window_handles
        #print('first_window ')
        #print(first_window)
        elem.click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(win_handles))
        two_windows = set(driver.window_handles)
        #print('two_windows ')
        #print(two_windows)
        two_windows.remove(first_window)
        #print('two_windows remove(first_window) ')
        #print(two_windows)
        for elem in two_windows:
            second_window = elem
        driver.switch_to_window(second_window)
        time.sleep(4)
        driver.close()
        time.sleep(2)
        driver.switch_to_window(first_window)



    #for elem in box:
    #    elem.click()

    #driver.window_handles
    #driver.current_window_handle
    #driver.switch_to_window('CDwindow-28243FBBB7589400895C45D4A8BE9E9E')
    #driver.close()












