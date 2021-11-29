import pytest
import time
from Basic.driver import shopkeeper_driver
from Basic.base import Base


@pytest.fixture(scope="class", name="driver")
def init_driver():
    driver = shopkeeper_driver()
    return driver


@pytest.fixture(scope="class")
def launch_app(driver):
    Base(driver).launch_app(page_description="启动火掌柜")
    time.sleep(8)
    yield
    driver.quit()
