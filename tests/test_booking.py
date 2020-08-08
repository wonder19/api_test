import pytest

from common.schema import post_booking_schema
from model.booking import BookingData
from model.booking import IncorrectBookingData
from utils.utils import is_validate


def test_create_booking_auth_client(auth_client):
    booking_data = BookingData().random()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200
    assert is_validate(res.json(), post_booking_schema)


@pytest.mark.parametrize("deposit_paid", ["true", "false"])
def test_create_booking_paid_unpaid(auth_client, deposit_paid):
    booking_data = BookingData().random()
    booking_data.depositpaid = deposit_paid
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200


def test_create_booking_unauth_client(unauth_client):
    booking_data = BookingData().random()
    res = unauth_client.create_booking(booking_data)
    assert res.status_code == 200
    assert is_validate(res.json(), post_booking_schema)


def test_incorrect_scheme(auth_client):
    booking_data = BookingData().random()
    booking_data.totalprice = 500
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200


def test_create_booking_without_data(auth_client):
    booking_data = BookingData()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 500


def test_create_booking_with_incorrect_json(auth_client):
    booking_data = IncorrectBookingData()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 500
