from enum import verify

import pytest
import requests
import allure_pytest
import json

from Constant.api_constant import URLS
from Helpers.api_request_wrapper import postreq
from Helpers.payload_manager import Createbooking
from Helpers.common_verification import *
from utilits.utilis import utils


class test_createbooking():
    def test_createbooking_positive(self):
        response = postreq(url=URLS.url_createbooking(),auth=None,header=utils.common_header(),payload=Createbooking,in_json=False)
        verify_statuscode(resposne_data=response,excepetd_data=200)

