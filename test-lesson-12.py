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
    driver.get("http://localhost/litecart/admin/")
    driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-apps-menu")))

    driver.find_element_by_css_selector('#box-apps-menu a[href*="catalog"]').click()
    driver.find_element_by_css_selector('#content a[href*="edit_product"]').click()

    time.sleep(2)

    pr_data = ['Umbrella', 'umbr', '03/24/2018', '04/24/2018', 'umbrella rain', 'I\'ll be  short: umbrella for you',\
         'Description for umbrella. a collapsible shade for protection against weather consisting of fabric stretched \
         over hinged ribs radiating from a central pole; especially : a small one for carrying in the hand'\
               , 'Head title of umbrella', 'Meta description of umbrella']

    img_file = os.path.abspath('8-zontik-1.jpg')

    driver.find_element_by_css_selector('#tab-general input[name="new_images[]"]').send_keys(img_file)
    driver.find_element_by_css_selector('#tab-general input[name="status"][value="1"]').click()
    driver.find_element_by_css_selector('#tab-general input[name="name[en]"]').send_keys(pr_data[0])
    driver.find_element_by_css_selector('#tab-general input[name="code"]').send_keys(pr_data[1])
    driver.find_element_by_css_selector('#tab-general input[name="date_valid_from"]').send_keys(pr_data[2])
    driver.find_element_by_css_selector('#tab-general input[name="date_valid_to"]').send_keys(pr_data[3])
    driver.find_element_by_css_selector('#content a[href*="#tab-information"]').click()

    time.sleep(2)

    # main_menu = driver.find_element_by_css_selector('#tab-information select[name="manufacturer_id"]')
    # main_menu.click()
    sub_menu = driver.find_element_by_css_selector('#tab-information select[name="manufacturer_id"] option[value="1"]')
    sub_menu.click()
    # ActionChains(driver).move_to_element(main_menu).click(sub_menu).perform()
    driver.find_element_by_css_selector('#tab-information input[name="keywords"]').send_keys(pr_data[4])
    driver.find_element_by_css_selector('#tab-information input[name = "short_description[en]"]').send_keys(pr_data[5])
    driver.find_element_by_css_selector('#tab-information div[contenteditable="true"]').send_keys(pr_data[6])
    driver.find_element_by_css_selector('#tab-information input[name = "head_title[en]"]').send_keys(pr_data[7])
    driver.find_element_by_css_selector('#tab-information input[name = "meta_description[en]"]').send_keys(pr_data[8])

    # prices

    driver.find_element_by_css_selector('#content a[href*="#tab-prices"]').click()

    time.sleep(2)

    driver.find_element_by_css_selector('#tab-prices input[name = "purchase_price"]').clear()
    driver.find_element_by_css_selector('#tab-prices input[name = "purchase_price"]')\
        .send_keys(Keys.HOME + '15')
    driver.find_element_by_css_selector('#tab-prices select[name = "purchase_price_currency_code"]')\
        .send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.TAB)

    driver.find_element_by_css_selector('#tab-prices input[name = "prices[USD]"]').clear()
    driver.find_element_by_css_selector('#tab-prices input[name = "prices[USD]"]') \
        .send_keys(Keys.HOME + '15')

    #driver.find_element_by_css_selector('#tab-prices input[name = "gross_prices[USD]"]').clear()
    #driver.find_element_by_css_selector('#tab-prices input[name = "gross_prices[USD]"]') \
    #    .send_keys(Keys.HOME + '17')

    driver.find_element_by_css_selector('#tab-prices input[name = "prices[EUR]"]').clear()
    driver.find_element_by_css_selector('#tab-prices input[name = "prices[EUR]"]') \
        .send_keys(Keys.HOME + '20')

    #driver.find_element_by_css_selector('#tab-prices input[name = "gross_prices[EUR]"]').clear()
    #driver.find_element_by_css_selector('#tab-prices input[name = "gross_prices[EUR]"]')\
    #   .send_keys(Keys.HOME + '25')

    driver.find_element_by_css_selector('#content button[name = "save"]').click()

    time.sleep(2)

    assert is_element_present(driver, By.CSS_SELECTOR, '#notices .success') is True

    box = driver.find_elements_by_css_selector('#content tbody td a')
    for elem in box:
        if elem.text == 'Umbrella':
            elem.click()
            break
    time.sleep(2)

    assert is_element_present(driver, By.CSS_SELECTOR, '#tab-general input[name="name[en]"]') is True

    time.sleep(2)








