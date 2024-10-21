import pytest
import allure_pytest
import requests


def Createbooking():
    payload = {
        "firstname": "Venkatsai",
        "lastname": "Nagula",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def createtoken():

    payload = {
        username : "admin",
        password : "password123"
    }
    return payload