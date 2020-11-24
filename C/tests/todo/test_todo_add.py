import pytest

from ..headers import *
import requests
import json
from .todos_data import *


@pytest.mark.monitor_test
def test_add_10_todo(app):
    for _ in range(1000):
        pass


def test_add_100_todo(app):
    pass


def test_add_1000_todo(app):
    pass
