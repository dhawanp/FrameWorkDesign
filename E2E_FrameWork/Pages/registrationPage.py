class registration:

    def __init__(self,driverObj):
        global driver
        driver=driverObj

    def enterFirstname(self,locatorValue,data):
        driver.find_element_by_name(locatorValue).send_keys(data)