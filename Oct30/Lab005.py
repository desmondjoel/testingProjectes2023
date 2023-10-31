#Convert to Dict JSON Response and Print

dict1= {

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}

print("Booking Id :",dict1["bookingid"])
print("checkin :",dict1["booking"]["bookingdates"]["checkin"])
print("checkout :",dict1["booking"]["bookingdates"]["checkout"])
