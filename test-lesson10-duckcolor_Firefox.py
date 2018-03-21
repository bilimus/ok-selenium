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
    # wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    # wd = webdriver.Edge()
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla Firefox\\firefox.exe")
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

    box = driver.find_element_by_id("box-campaigns")

    pr_reg_color = box.find_element_by_css_selector('.regular-price').value_of_css_property('color')
    pr_reg_color = Color.from_string(pr_reg_color).hex

    # Сравниваем равность по значению 3 цветов, серый цвет
    assert pr_reg_color[1:3] == pr_reg_color[3:5]
    assert pr_reg_color[5:7] == pr_reg_color[3:5]

    pr_camp_color = box.find_element_by_css_selector('.campaign-price').value_of_css_property('color')
    pr_camp_color = Color.from_string(pr_camp_color).hex

    # Тест 2 цветов на равенсто 0, красный цвет
    assert pr_camp_color[5:7] == '00'
    assert pr_camp_color[3:5] == '00'

    pr_reg_font_size = box.find_element_by_css_selector('.regular-price').value_of_css_property('font-size')
    pr_camp_font_size = box.find_element_by_css_selector('.campaign-price').value_of_css_property('font-size')


    # Проверка размеров шрифтов спец цена больше обычной
    assert float(pr_camp_font_size[:-2]) > float(pr_reg_font_size[:-2])

    # тест наличия зачеркнутой обычной цены
    assert is_element_present(box, By.CSS_SELECTOR,'s.regular-price') is True

    # Тест на жирность шрифта
    assert is_element_present(box, By.CSS_SELECTOR, 'strong.campaign-price') is True

    pr_name = box.find_element_by_css_selector('.name').text
    pr_reg_price = box.find_element_by_css_selector('.regular-price').text
    pr_camp_price = box.find_element_by_css_selector('.campaign-price').text

    # Переходим на страницу продукта
    box.find_element_by_tag_name("a").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-product")))

    box = driver.find_element_by_id('box-product')

    snd_name = box.find_element_by_css_selector('h1.title').text
    snd_reg_price = box.find_element_by_css_selector('.regular-price').text
    snd_camp_price = box.find_element_by_css_selector('.campaign-price').text

    # Проверка равенста имени продукта, обычной и спец цены из разных страниц
    assert pr_name == snd_name
    assert pr_reg_price == snd_reg_price
    assert pr_camp_price == snd_camp_price

    # тест наличия зачеркнутой обычной цены
    assert is_element_present(box, By.CSS_SELECTOR, 's.regular-price') is True

    # Тест на жирность шрифта
    assert is_element_present(box, By.CSS_SELECTOR, 'strong.campaign-price') is True

    snd_reg_font_size = box.find_element_by_css_selector('.regular-price').value_of_css_property('font-size')
    snd_camp_font_size = box.find_element_by_css_selector('.campaign-price').value_of_css_property('font-size')

    # Проверка размеров шрифтов спец цена больше обычной
    assert float(snd_camp_font_size[:-2]) > float(snd_reg_font_size[:-2])

    snd_reg_color = box.find_element_by_css_selector('.regular-price').value_of_css_property('color')
    snd_reg_color = Color.from_string(pr_reg_color).hex

    # Сравниваем равность по значению 3 цветов (серый цвет)
    assert snd_reg_color[1:3] == snd_reg_color[3:5]
    assert snd_reg_color[5:7] == snd_reg_color[3:5]

    snd_camp_color = box.find_element_by_css_selector('.campaign-price').value_of_css_property('color')
    snd_camp_color = Color.from_string(pr_camp_color).hex

    # Тест 2 цветов на равенсто 0, красный цвет
    assert snd_camp_color[5:7] == '00'
    assert snd_camp_color[3:5] == '00'

    time.sleep(2)
















