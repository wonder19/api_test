from model.booking import BookingData


def test_create_booking(auth_client):
    booking_data = BookingData().random()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200
