from selenium import webdriver

wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
print(wd.capabilities)
wd.get("http://www.beststudy.info")
wd.quit()