import requests
import json

# get the base url
base_url= 'https://reqres.in/api'

# AUTHENTICATION TOKEN
auth_token= "put token value here if available"

def get_request():
    url = base_url + "/users"
    print("get url: "+url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json Get response body:", json_str)
    print("Successfully print")


# calling function
get_request()