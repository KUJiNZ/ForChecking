import pytest
import requests
import json


def test_api():
    url = 'https://reqres.in/api/register'

    data = {"email": "eve.holt@reqres.in","password": "pistol"}

    res = requests.post(url,data = data)

    jres = json.loads(res.text)

    assert res.status_code == 200

    assert jres["id"] == 4
    assert jres['token'] == 'QpwL5tke4Pnpja7X4'


