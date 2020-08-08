from model.booking import BookingData


def test_update_booking(auth_client, create_booking):
    booking_data = BookingData().random()
    booking_id = create_booking.get("bookingid")
    res = auth_client.update_booking(booking_data, booking_id)
    assert res.status_code == 200
    assert create_booking != res.json()


def test_update_booking_invalid_id(auth_client, create_booking):
    non_exist_id = 1000
    booking_data = BookingData().random()
    res = auth_client.update_booking(booking_data, non_exist_id)
    assert res.status_code == 405
