import  requests
import pytest


def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    hed={"Content-Type" : "application/json"}
    json_data={
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }

    req=requests.post(URL,headers=headers,json=json_data)
    #req=requests.post(url=URL, headers=headers, json=json_payload)
    #req=requests.post(url=URL,headers,json_payload)
    print(type(hed))
    print(type(json_data))
    data =req.status_code
    print(data)
    print(req.json())

create_booking()
