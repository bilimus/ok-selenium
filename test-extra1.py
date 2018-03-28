import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
    # driver.delete_all_cookies()
    driver.get("http://localhost/litecart/")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    box = driver.find_element_by_id("logotype-wrapper")
    box.find_element_by_tag_name("a").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    ducks = driver.find_elements_by_class_name("product")
    ducks[0].find_element_by_tag_name("a").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "add_cart_product")))
    driver.find_element_by_name("add_cart_product").click()
    time.sleep(1)
    #driver.refresh()

    #driver.implicitly_wait(5)
    #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "formatted_value")))

    cart = driver.find_element_by_id("cart")
    checkout = cart.find_elements_by_tag_name("a")
    checkout[2].click()
    time.sleep(3)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))



