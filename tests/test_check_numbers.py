# Test to check the number format inputted by user
import sys

sys.path.append("..")
from app.functions import check_numbers


def test_time_format():
    time_format = check_numbers.check_phone_number(254714300892)
    assert time_format == True


def test_choice():
    assert check_numbers.check_options("1") == True
