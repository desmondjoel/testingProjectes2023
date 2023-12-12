import requests

URL = "https://restful-booker.herokuapp.com/booking"
headers = {"Content-Type": "application/json"}
json_payload = {
    "firstname": "Amit",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}
response = requests.post(url=URL, headers=headers, json=json_payload)
print(response.status_code)