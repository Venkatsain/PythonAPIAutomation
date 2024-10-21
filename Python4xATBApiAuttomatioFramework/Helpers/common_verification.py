import pytest
import requests
import allure_pytest


def verify_statuscode(resposne_data,excepetd_data):
    assert resposne_data.status.code == excepetd_data

def verify_key(key,excepetd_data):
    assert key == excepetd_data

def verify_key_not_null(key):
    assert key != 0
    assert key > 0
def json_key_not_null_token(key):
    assert key != 0