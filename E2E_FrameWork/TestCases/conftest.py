from E2E_FrameWork.Base import initialiseDriver
import pytest
import time

@pytest.fixture()
def setup(request):
    driver = initialiseDriver.startBrowser("http://way2automation.com/way2auto_jquery/draggable.php#load_box")
    request.cls.driver=driver


    yield
    time.sleep(5)
    driver.quit()