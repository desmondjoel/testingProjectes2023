import pytest
import requests
import json


def generateToken():
    url="https://restful-booker.herokuapp.com/booking/1"
    response=requests.get(url)
    tt=response.text
    print(tt)
    print(response.json())
    print(response.status_code)
    if(response.status_code==200):
        print("test is successfull")
    else:
        print("test failed")

generateToken()
