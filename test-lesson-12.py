import time
import pytest
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

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-apps-menu")))

    pr_data = ['Umbrella', 'umbr', 'images/products/8-zontik-1.jpg', '03/24/2018', '04/24/2018']

    driver.find_element_by_css_selector('#box-apps-menu a[href*="catalog"]').click()
    driver.find_element_by_css_selector('#content a[href*="edit_product"]').click()

    driver.find_element_by_css_selector('#tab-general input[name="name[en]"]').send_keys(pr_data[0])
    driver.find_element_by_css_selector('#tab-general input[name="code"]').send_keys(pr_data[1])
    # driver.find_element_by_css_selector('#tab-general input[name="new_images[]"]').send_keys(pr_data[2])
    driver.find_element_by_css_selector('#tab-general input[name="date_valid_from"]').send_keys(pr_data[3])
    driver.find_element_by_css_selector('#tab-general input[name="date_valid_to"]').send_keys(pr_data[4])
    driver.find_element_by_css_selector('#content a[href*="#tab-information"]').click()
    # main_menu = driver.find_element_by_css_selector('#tab-information select[name="manufacturer_id"]')
    # main_menu.click()
    sub_menu = driver.find_element_by_css_selector('#tab-information select[name="manufacturer_id"] option[value="1"]')
    sub_menu.click()
    # ActionChains(driver).move_to_element(main_menu).click(sub_menu).perform()
    
    time.sleep(5)










