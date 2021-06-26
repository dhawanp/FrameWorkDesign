import configparser
def readConfig(section,key):
    reader=configparser.ConfigParser()
    reader.read("C:\\Users\\windows\\PycharmProjects\\FrameWorkDesign\\E2E_FrameWork\\ConfigurationData\\locators.cfg")
    return reader.get(section,key)

# a=readConfig()
# print(a)