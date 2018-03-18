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
    # driver.get("http://localhost/litecart/admin/")
    # driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sidebar")))

    box = driver.find_element_by_id("box-apps-menu-wrapper")
    menu = box.find_elements_by_xpath(".//a[@href]")
    length = len(menu)

    for i in range(length):
        menu[i].click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sidebar")))
        box = driver.find_element_by_id("box-apps-menu-wrapper")

        if is_element_present(box, By.CSS_SELECTOR, "ul.docs"):
            docum = box.find_element_by_css_selector("ul.docs")
            men = docum.find_elements_by_xpath(".//a[@href]")
            men_l=len(men)

            for j in range(men_l):
                men[j].click()
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sidebar")))
                box = driver.find_element_by_id("box-apps-menu-wrapper")
                docum = box.find_element_by_css_selector("ul.docs")
                men = docum.find_elements_by_xpath(".//a[@href]")

        driver.get("http://localhost/litecart/admin/")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sidebar")))
        box = driver.find_element_by_id("box-apps-menu-wrapper")
        menu = box.find_elements_by_xpath(".//a[@href]")

