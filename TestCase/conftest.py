import pytest
from Baseic.driver import shopkeeper_driver


@pytest.fixture(scope="class")
def init_driver():
    driver = shopkeeper_driver()
    yield driver
