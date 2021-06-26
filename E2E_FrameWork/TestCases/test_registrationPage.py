from E2E_FrameWork.Base import initialiseDriver , configreader
from E2E_FrameWork.Pages import registrationPage
def test_reg():
    driver=initialiseDriver.startBrowser("http://way2automation.com/way2auto_jquery/registration.php#load_box")
    regpage=registrationPage.registration(driver)
    #configreader.readConfig("registeration_page","name")
    regpage.enterFirstname(configreader.readConfig("registeration_page","name"),"PRATEEK")