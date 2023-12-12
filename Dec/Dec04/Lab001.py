import requests
def generateToken():
    url="https://restful-booker.herokuapp.com/booking/1"
    response=requests.get(url)
    print(response.text)
    print(response.headers)
    assert response.status_code==200

    data =response.json()
    assert 'firstname' in data, "Firstnsme is not present"
    assert 'lastname' in data, "LastName is not present"

    assert data["firstname"] == "Eric", "Firstname is not"

generateToken()

#verify

