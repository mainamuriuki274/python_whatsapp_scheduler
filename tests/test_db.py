# test db functions
import sys

import pytest

sys.path.append("..")
from app.functions import db


@pytest.fixture(scope="module")
def connection():
    db_connection = db.sqlite_connect(':memory:')
    yield db_connection
    db_connection.close()


def test_create_table(connection):
    assert db.create_table(connection) == True


def test_insert_data(connection):
    assert db.insert_data(connection, ["31/06/2021 13:54", "Niaje Buda", 254714308092, "31/06/2021 15:54"]) == True


def test_select_data(connection):
    assert db.select_data(connection) == [(1, '31/06/2021 13:54', 'Niaje Buda', '254714308092', '31/06/2021 15:54')]
