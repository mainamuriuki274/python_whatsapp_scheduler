# Test to check the time format inputted by user
import sys

import pytest

sys.path.append("..")
from app.functions import date_time


def test_time_format():
    assert date_time.check_time_format("3:01") == True


def test_date_format():
    assert date_time.check_date_format("30/06/2021") == True


def test_get_todays_date():
    assert date_time.get_todays_date() == "01/07/2021"


def test_get_time_now():
    assert date_time.get_time_now() == "14:37"


def test_check_date_not_passed():
    assert date_time.check_date_not_passed("30/06/2021", "1/07/2021") == True


def test_check_date_time_not_passed():
    assert date_time.check_date_time_not_passed("30/06/2021 14:46:00", "1/07/2021 15:30:00") == True


def test_countdown_timer():
    assert date_time.check_date_time_not_passed("30/06/2021 14:46:00", "30/06/2021 14:47:00") == True
