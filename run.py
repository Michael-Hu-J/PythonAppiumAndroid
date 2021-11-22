import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system("adb connect 127.0.0.1:5555")
    os.system("allure generate ./allure_temp/ -o ./allure_report --clean")
