# test db functions
import sys

sys.path.append("..")
from app.functions import db


def test_sqlite_connect():
    assert db.sqlite_connect() != "Error! Failed to connect to db"



