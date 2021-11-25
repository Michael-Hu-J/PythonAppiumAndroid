import pytest
from Basic.driver import shopkeeper_driver


@pytest.fixture(scope="class", name="driver")
def init_driver():
    driver = shopkeeper_driver()
    return driver
    # driver.close_app()

