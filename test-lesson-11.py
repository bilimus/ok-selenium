import time
import pytest
from selenium.webdriver.common.keys import Keys
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
    wd = webdriver.Firefox(capabilities={"marionette": False})
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
    items = driver.find_elements_by_css_selector('select option')
    for elem in items:
        if elem.text == item:
            elem.click()
            break


def test_example(driver):
    # driver.get("http://localhost/litecart/admin/")
    driver.get("http://localhost/litecart/")
    driver.delete_all_cookies()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-campaigns")))

    driver.find_element_by_css_selector('#box-account-login table a').click()

    personal_data=['12-12345', 'Amazon-FB LLC', 'Mark', 'Bezos', '1 Hacker Way', '', '94025', 'Menlo Park','','', 'Mark.bezos@amazon-fb.com', '+1-123-123-4455','','', 'iamaseobitch', 'iamaseobitch','']

    box = driver.find_elements_by_css_selector('#create-account td')
    # заполняем некоторые поля
    for i in range(len(box)):
        if i not in (8,9,12,13,16):
            inpt = box[i].find_element_by_css_selector('input')
            inpt.clear()
            inpt.send_keys(Keys.HOME + personal_data[i] + Keys.TAB)
            time.sleep(0.1)

    choose_el(box[8], 'United States')
    time.sleep(2)
    choose_el(box[9], 'California')

    chk_box = box[12].find_element_by_css_selector('label input')
    if chk_box.is_selected():
        time.sleep(2)
        chk_box.click()
    # Создаем учетную запись, нажимаем на кнопку Create
    box[16].find_element_by_css_selector('button').click()

    time.sleep(3)
    # Зашли на персональную страницу и делаем Logout
    menu_items = driver.find_elements_by_css_selector('#box-account li a')
    for elem in menu_items:
        if elem.text == 'Logout':
            elem.click()
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







