import time
import pytest
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
    # driver.get("http://localhost/litecart/admin/")
    # driver.delete_all_cookies()
    driver.get("http://localhost/litecart/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-campaigns")))

    box = driver.find_elements_by_css_selector('#main .content a[class="link"]')
    for elem in box:
        assert is_element_present(elem, By.CSS_SELECTOR, '.sticker') is True
        num_stickers = elem.find_elements_by_css_selector('.sticker')
        assert len(num_stickers) == 1

    box = driver.find_elements_by_css_selector('#box-latest-products a[class="link"]')
    box[-1].click()
    if is_element_present(driver, By.CSS_SELECTOR, '#box-product select'):
        driver.find_element_by_css_selector('#box-product select option[value="Medium"]').click()

    time.sleep(5)









