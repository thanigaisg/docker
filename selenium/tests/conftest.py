import pytest
import os
import time


driver = None

@pytest.fixture(scope='class')
def setup(request):
    request.cls.os.system("call ../start_dockergrid.bat")
    request.cls.time.sleep(120)
    yield
    global driver
    driver = request.cls.driver
    driver.close()
    request.cls.os.system("call ../stop_dockergrid.bat")
    request.cls.os.system("taskkill /f /im cmd.exe")

