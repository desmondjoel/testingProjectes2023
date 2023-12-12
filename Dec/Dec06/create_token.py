import requests
import pytest

def create_token():
    url="https://restful-booker.herokuapp.com/auth"
    hed={"Content-Type" : "application/json"}
    json_payload={
        "username" : "admin",
        "password" : "password123"
    }
    response= requests.post(url=url,headers=hed,json=json_payload)
    data=response.json()
    tok=data["token"]
    print(tok)
    print(data)
    return tok

create_token()

def put_request(bookid):
    url="https://restful-booker.herokuapp.com/booking/"
    put_url=url+str(bookid)
    cookie_value="token="+create_token()
    hed = {"Content-Type": "application/json",
           "Cookie": cookie_value
           }
    print(hed)
    json_payoad={
        "firstname" : "Joel",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.put(url=put_url, headers=hed, json=json_payoad)
    data=response.status_code
    print(response.text)
    print(data)

#
put_request(2742)

def delete_request(bookid):
    url="https://restful-booker.herokuapp.com/booking/"
    put_url=url+str(bookid)
    cookie_value="token="+create_token()
    hed = {"Content-Type": "application/json",
           "Cookie": cookie_value
           }
    print(hed)
    response = requests.delete(url=put_url, headers=hed)
    data=response.status_code
    print(data)

delete_request(4039)