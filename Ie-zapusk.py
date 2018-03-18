from selenium import webdriver

wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
wd.get("http://google.com")
wd.quit()