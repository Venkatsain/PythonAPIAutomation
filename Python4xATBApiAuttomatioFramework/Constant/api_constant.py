import pytest
import requests
import allure_pytest
import json


class URLS ():
    def url_base(self):
        return "https://restful-booker.herokuapp.com"
    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_createbooking(self):
        return "https://restful-booker.herokuapp.com/booking"

    #Update put [tach deete url

    def url_put_delete_patch(self,Bookingid):
        return "https://restful-booker.herokuapp.com/booking/" + str(Bookingid)