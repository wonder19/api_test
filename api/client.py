import requests

from model.booking import BookingData
from model.login_auth import UserData
from utils.utils import logging as log


class Client:
    s = requests.Session()

    def __init__(self, url):
        self.url = url

    def auth(self, user_data: UserData):
        data = user_data.__dict__
        return self.s.post(self.url + "/auth", json=data)

    def set_cookies(self, user_data: UserData):
        res = self.auth(user_data)
        token = res.json().get("token")
        cookie = requests.cookies.create_cookie("token", token)
        self.s.cookies.set_cookie(cookie)

    @log("CREATING BOOKING")
    def create_booking(self, booking_data: BookingData):
        booking = booking_data.object_to_dict()
        return self.s.post(self.url + "/booking", json=booking)

    @log("UPDATE BOOKING")
    def update_booking(self, booking_data: BookingData, booking_id):
        booking = booking_data.object_to_dict()
        return self.s.put(self.url + f"/booking/{booking_id}", json=booking)

    def get_booking_id(self):
        return self.s.get(self.url + f"/booking")
