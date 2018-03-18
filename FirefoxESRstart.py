# Запуск FirefoxESR по старому методу
from selenium import webdriver
wd = webdriver.Firefox(capabilities={"marionette": False})


