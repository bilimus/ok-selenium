# новая схема:
from selenium import webdriver

wd = webdriver.Firefox()
# новая схема более явно:
wd = webdriver.Firefox(capabilities={"marionette": True})
# старая схема:
wd = webdriver.Firefox(capabilities={"marionette": False})



# Указание пути к браузеру

wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
