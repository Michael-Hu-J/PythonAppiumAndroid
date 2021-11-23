import pytest
from Basic.driver import shopkeeper_driver


@pytest.fixture(scope="package", name="driver")
def init_driver():
    driver = shopkeeper_driver()
    return driver
