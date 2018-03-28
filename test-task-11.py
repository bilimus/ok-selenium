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

def choose_el(driver, item):
    items = driver.find_elements_by_css_selector('option')
    for elem in items:
        if elem.text == item:
            elem.click()
            break

def manipulations(driver, arg, elem):
    input_box = driver.find_element_by_css_selector('input[name="' + arg + '"]')
    input_box.clear()
    input_box.send_keys(Keys.HOME + elem + Keys.TAB)
    time.sleep(0.2)

def test_example(driver):
    # driver.get("http://localhost/litecart/admin/")
    driver.get("http://localhost/litecart/")
    driver.delete_all_cookies()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-campaigns")))

    personal_data = ['12-12345', 'Amazon-FB LLC', 'Mark', 'Bezos', '1 Hacker Way', 'apt 9', '94025', 'Menlo Park', '', '',
                     '', '+1-123-123-4455', '', '', 'iamaseobitch', 'iamaseobitch', '']
    personal_data[10] = str(uuid.uuid4()) + '@fb.com'

#field_dict = {'12-12345': 'tax-id', 'Amazon-FB LLC': 'company' , 'Mark' : 'firstname', 'Bezos' : 'lastname',\
#              '1 Hacker Way' : 'address1', 'apt 9' : 'address2', '94025':'postcode', 'Menlo Park': 'city', \
#              personal_data[10]: 'email', '+1-123-123-4455': 'phone', 'password': 'password', 'password' : 'confirmed_password'}

    driver.find_element_by_css_selector('#box-account-login table a').click()
    time.sleep(2)
    box = driver.find_element_by_css_selector('#create-account')
    # заполняем некоторые поля

    manipulations(box, 'tax_id', personal_data[0])
    manipulations(box, 'company', personal_data[1])
    manipulations(box, 'firstname', personal_data[2])
    manipulations(box, 'lastname', personal_data[3])
    manipulations(box, 'address1', personal_data[4])
    manipulations(box, 'address2', personal_data[5])
    manipulations(box, 'postcode', personal_data[6])
    manipulations(box, 'city', personal_data[7])
    manipulations(box, 'email', personal_data[10])
    manipulations(box, 'phone', personal_data[11])
    manipulations(box, 'password', personal_data[14])
    manipulations(box, 'confirmed_password', personal_data[15])

    choose_el(driver.find_element_by_css_selector('#create-account select[name="country_code"]'), 'United States')
    time.sleep(2)
    choose_el(driver.find_element_by_css_selector('#create-account select[name="zone_code"]'), 'California')

    chk_box = driver.find_element_by_css_selector('#create-account input[name="newsletter"]')
    if chk_box.is_selected():
        time.sleep(2)
        chk_box.click()
    # Создаем учетную запись, нажимаем на кнопку Create
    driver.find_element_by_css_selector('#create-account button').click()

    time.sleep(3)
    # Зашли на персональную страницу и делаем Logout
    menu_items = driver.find_elements_by_css_selector('#box-account li a')
    for elem in menu_items:
        if elem.text == 'Logout':
            elem.click()
    time.sleep(2)

    assert is_element_present(driver, By.CSS_SELECTOR, '#main') is True

    # Пробуем логиниться вводим ел.почту
    login_ = driver.find_element_by_css_selector('#box-account-login input[name=email')
    login_.clear()
    login_.send_keys(personal_data[10])

    time.sleep(2)
#    Вводим пароль
    login_ = driver.find_element_by_css_selector('#box-account-login input[name=password')
    login_.clear()
    login_.send_keys(personal_data[14])
#    кликаем по кнопке логин
    login_ = driver.find_element_by_css_selector('#box-account-login button[name=login')
    login_.click()
    time.sleep(2)
    assert is_element_present(driver, By.CSS_SELECTOR, '#main') is True

    menu_items = driver.find_elements_by_css_selector('#box-account li a')
    for elem in menu_items:
        if elem.text == 'Logout':
            elem.click()
    time.sleep(2)

    assert is_element_present(driver, By.CSS_SELECTOR, '#main') is True

