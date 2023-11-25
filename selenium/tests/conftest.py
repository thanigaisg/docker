import subprocess
import pytest
import os
import time


driver = None


@pytest.fixture(scope='class')
def setup(request):
    subprocess.Popen(["call", "../start_dockergrid.bat"], shell=True, cwd=os.getcwd())
    print("Docker Grid Started")
    time.sleep(60)

    yield

    subprocess.Popen(["call", "../stop_dockergrid.bat"], shell=True, cwd=os.getcwd())
    print("Docker Grid Stopped")