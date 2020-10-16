from venmo_api import Client
import requests
import json

# access_token = Client.get_access_token(username='mateos.main@gmail.com',
#                                        password='blackBAG55')

# venmo = Client(access_token=access_token)

# token = "Bearer ...."   #  this should be your access token


def get_my_balance(token):
    header = {
        "Authorization": token,
        "User-Agent": "Venmo/8.6.1 (iPhone; iOS 13.0; Scale/3.0)"
    }
    url = "https://api.venmo.com/v1/account"
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("Something went wrong, check the logs")
        print(response.status_code, response.reason, response.text)
        return 0

    json = response.json()
    return float(json.get('data').get('user-id'))


print(get_my_balance("Bearer 21a4a783390e6473278b862bd765de81d96b2f0175f9283377ec8beb875f2fed"))

def get_my_info(token):
    header = {
        
    }

