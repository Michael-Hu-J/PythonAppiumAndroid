import pytest
import allure
import os


class TestClass:
    @pytest.mark.usefixtures("my_fixture")
    @pytest.mark.smoke
    def test_one(self, my_fixture):
        # print("\n---test_one---")
        print(my_fixture)

    @pytest.mark.parametrize("a, b", [("3+5", 9), ("3*5", 15)])
    @pytest.mark.username
    def test_two(self, a, b):
        assert eval(a) == b
        print("\n---test_two---")

    @pytest.mark.password
    def test_three(self):
        print("\n密码")


