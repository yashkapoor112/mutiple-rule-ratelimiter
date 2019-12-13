import requests
from datetime import date, timedelta
import pytest
from pytest_mock import mocker


from kills.builders.test_builder import DragonBuilder


class TestCamstasks:

    @pytest.fixture
    def dragon(self):
        return DragonBuilder().get_dragon()

    def test_register_dragon(self, mocker, dragon):

        #sample