import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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

def main_page_load(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "countries_form")))
    list_of_c = driver.find_element_by_name('countries_form')
    return list_of_c.find_elements_by_css_selector('td')


def test_example(driver):
    # driver.get("http://localhost/litecart/admin/")
    # driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sidebar")))

    tds = main_page_load(driver)

    len_tds = len(tds)
    for i in range(11, len_tds):
        if i % 7 == 4:
            assert tds[i-7].text < tds[i].text
            if tds[i-6].text != '0':
                tds[i-7].find_element_by_tag_name('a').click()
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "table-zones")))
                sublist = driver.find_element_by_id('table-zones')
                sub_tds = sublist.find_elements_by_tag_name('td')
                sub_len_tds = len(sub_tds)

                for j in range(6, sub_len_tds-2, 4):
                    assert sub_tds[j-4].text < sub_tds[j].text
                tds = main_page_load(driver)




    # countries = list.find_elements_by_tag_name('a')
    # for i in range(2, len(countries), 2):
    #    assert countries[i-2].text < countries[i].text
    # tds = list.find_elements_by_css_selector('td[cellIndex=5]')