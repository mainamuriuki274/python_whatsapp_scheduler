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


def test_create_tables(connection):
    assert db.create_tables(connection) == True


def test_insert_messages(connection):
    assert db.insert_messages(connection, ["31/06/2021 13:54", "Niaje Buda", 254714308092, "31/06/2021 15:54"]) == True


def test_select_messages(connection):
    assert db.select_messages(connection) == [(1, '31/06/2021 13:54', 'Niaje Buda', '254714308092', '31/06/2021 15:54')]


def test_insert_contacts(connection):
    assert db.insert_contacts(connection, ["clients", "[254714308092,254789152368]"]) == True


def test_select_numbers(connection):
    assert db.select_numbers(connection) == [(1, "clients", "[254714308092,254789152368]")]


def test_select_number(connection):
    assert db.select_number(connection, "clients") == [(1, "clients", "[254714308092,254789152368]")]
