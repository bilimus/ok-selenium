import time
import pytest
import sys, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
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
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get('http://localhost/litecart/admin')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#box-login button[name="login"]')))
    time.sleep(1)
    driver.find_element_by_css_selector('#box-login input[name="username"]').send_keys('admin')
    driver.find_element_by_css_selector('#box-login input[name="password"]').send_keys('admin')
    time.sleep(1)
    driver.find_element_by_css_selector('#box-login button[name="login"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#box-apps-menu a[href*="catalog"]')))
    time.sleep(1)
    driver.find_element_by_css_selector('#box-apps-menu a[href*="catalog"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content a[href*="edit_product"]')))
    time.sleep(1)
    driver.find_element_by_css_selector('#content a[href*="edit_product"]').click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab-general input[name="status"]')))
    driver.find_element_by_css_selector('#tab-general input[name="status"]').click()
    driver.find_element_by_css_selector('#tab-general input[name="name[en]"]').send_keys('name-zayka')
    driver.find_element_by_css_selector('#tab-general input[name="code"]').send_keys('code-zayka')
    driver.find_element_by_css_selector('#tab-general input[data-name="Rubber Ducks"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#tab-general input[data-name="Subcategory"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab-general select option')))
    box = driver.find_elements_by_css_selector('#tab-general select[name="default_category_id"] option')
    for elem in box:
        if elem.text == 'Subcategory':
            elem.click()
            break
    driver.find_element_by_css_selector('#tab-general input[name="product_groups[]"][value="1-3"]').click()
    driver.find_element_by_css_selector('#tab-general input[name="quantity"]').clear()
    driver.find_element_by_css_selector('#tab-general input[name="quantity"]').send_keys('15')
    box = driver.find_elements_by_css_selector('#tab-general select[name="sold_out_status_id"] option')
    for elem in box:
        if elem.text == 'Temporary sold out':
            elem.click()
            break

    img_file = os.path.abspath('zaya.png')
    driver.find_element_by_css_selector('#tab-general input[name="new_images[]"]').send_keys(img_file)
    # driver.find_element_by_css_selector('#tab-general input[name="date_valid_from"]').clear()
    driver.find_element_by_css_selector('#tab-general input[name="date_valid_from"]')\
                                                                    .send_keys(Keys.HOME + '04/01/2018')
    driver.find_element_by_css_selector('#tab-general input[name="date_valid_to"]') \
                                                                     .send_keys(Keys.HOME + '05/01/2018')

    driver.find_element_by_css_selector('#content a[href*="#tab-information"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab-information input[name="keywords"]')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="manufacturer_id"] option[value="1"]')))
    driver.find_element_by_css_selector('select[name="manufacturer_id"] option[value="1"]').click()
    driver.find_element_by_css_selector('#tab-information input[name="keywords"]')\
        .send_keys('keywords_AAAA' + Keys.TAB + 'shortdesc_Zaya' + Keys.TAB + 'desc_Zaya_with_flowers' + Keys.TAB + 'headtitle_Zayka' + Keys.TAB + 'meta_Ogogo')

    driver.find_element_by_css_selector('#content a[href*="#tab-prices"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab-prices input[name="purchase_price"]')))
    driver.find_element_by_css_selector('#tab-prices input[name="purchase_price"]').clear()
    driver.find_element_by_css_selector('#tab-prices input[name="purchase_price"]').send_keys('30')
    box = driver.find_elements_by_css_selector('#tab-prices select[name="purchase_price_currency_code"] option')
    for elem in box:
        if elem.text == 'US Dollars':
            elem.click()
            break
    driver.find_element_by_css_selector('#tab-prices input[name="prices[USD]"]').send_keys('30')
    driver.find_element_by_css_selector('#tab-prices input[name="prices[EUR]"]').send_keys('27')
    driver.find_element_by_css_selector('button[name="save"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content a')))
    box = driver.find_elements_by_css_selector('#content a')
    for elem in box:
        if elem.text == 'name-zayka':
            elem.click()
            break
    time.sleep(7)







