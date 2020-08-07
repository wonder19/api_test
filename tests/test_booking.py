import pytest

from model.booking import BookingData


def test_create_booking_auth_client(auth_client):
    booking_data = BookingData().random()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200


@pytest.mark.parametrize('deposit_paid', ['true', 'false'])
def test_create_booking_paid_unpaid(auth_client, deposit_paid):
    booking_data = BookingData().random()
    booking_data.depositpaid=deposit_paid
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200


def test_create_booking_unauth_client(unauth_client):
    booking_data = BookingData().random()
    res = unauth_client.create_booking(booking_data)
    assert res.status_code == 200


def test_incorrect_scheme(auth_client):
    booking_data = BookingData().random()
    booking_data.totalprice=None
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 500


def test_create_booking_without_data(auth_client):
    booking_data = BookingData()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 500