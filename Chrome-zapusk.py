from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("start-maximized")

wd = webdriver.Chrome(chrome_options=options)
wd.quit()