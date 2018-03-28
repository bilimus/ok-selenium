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

def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False

def test_example(driver):

    for i in range(3):
        driver.get("http://localhost/litecart/")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-most-popular a")))
        driver.find_element_by_css_selector("#box-most-popular a").click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                                   '#box-product button[name="add_cart_product"]')))

        if is_element_present(driver, By.CSS_SELECTOR, '#box-product select[name="options[Size]"]'):
            size = driver.find_element_by_css_selector('#box-product select[name="options[Size]"]')
            size.find_element_by_css_selector('option[value="Small"]').click()

        duck_text = driver.find_element_by_css_selector('#cart span[class="quantity"]').text

        driver.find_element_by_css_selector('#box-product button[name="add_cart_product"]').click()

        wait = WebDriverWait(driver, 5)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart .quantity'), str(int(duck_text)+1)))

    driver.find_element_by_css_selector("#cart a").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                        '#box-checkout-cart button[name="remove_cart_item"]')))

    for i in range(3):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,\
                                                     '#box-checkout-cart  button[name="remove_cart_item"]')))
        driver.find_element_by_css_selector('#box-checkout-cart  button[name="remove_cart_item"]').click()
        driver.refresh()
        if not is_element_present(driver, By.CSS_SELECTOR,'#box-checkout-cart  button[name="remove_cart_item"]'):
            break
    time.sleep(2)
