from selenium import webdriver

def startBrowser(url):
    global driver
    driver=webdriver.Chrome('C:\\Users\windows\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.quit()