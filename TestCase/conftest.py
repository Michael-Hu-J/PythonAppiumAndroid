import pytest
from Basic.driver import shopkeeper_driver
from Basic.base import Base


@pytest.fixture(scope="class", name="driver")
def init_driver():
    driver = shopkeeper_driver()
    return driver
    # driver.close_app()

@pytest.fixture(scope="class")
def launch_app():
    driver = init_driver()
    Base(driver).launch_app(page_description="启动火掌柜")

