from selenium.webdriver.common.action_chains import ActionChains
class draggable:

    def __init__(self,driverObj):
        global driver
        driver=driverObj
    def clickonMainButton(self,locator):
        btn=driver.find_element_by_xpath(locator)
        btn.click()
    def switchToIframe(self,locator):
        iframe = driver.find_element_by_xpath(locator)
        driver.switch_to.frame(iframe)
    def findPositionOfDraggableElement(self,locator):
        a=driver.find_element_by_id(locator)
        location_1=a.location
        x=location_1.get('x')
        return x
    def dragAndDrop(self,drgStart):
        action=ActionChains(driver)
        a=driver.find_element_by_id(drgStart)
        action.drag_and_drop_by_offset(a,100,0)
        action.perform()



