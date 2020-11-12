from venmo_api import Client, AuthenticationApi, ApiClient
import datetime


def find_user_for_request(username, access_token):
    venmo = Client(access_token=access_token)
    users = venmo.user.search_for_users(query=username,
                                        page=1)
    for found_user in users:
        if found_user.username == username:
            return found_user.id
    return False


def request_friend(user_id, min_amount, access_token, note):
    venmo = Client(access_token=access_token)
    venmo.payment.request_money(
        min_amount, f"{note} - Create your own Venmo crowdfund with Crowdmo.io", user_id)


def venmo_get_otp(username, password, device_id):
    return Client.get_access_token(username=username, password=password, device_id=device_id)


def venmo_get_access_token(otp_secret, otp_code, device_id):
    authn_api = AuthenticationApi(api_client=ApiClient(), device_id=device_id)
    return authn_api.authenticate_using_otp(user_otp=otp_code, otp_secret=otp_secret)


def update_contributors(search_note, creation_date, access_token):
    donors = dict()
    venmo = Client(access_token=access_token)
    user = venmo.user.get_my_profile()
    transactions = venmo.user.get_user_transactions(user.id)
    timestamp = datetime.datetime.timestamp(creation_date)

    for transaction in transactions:
        if transaction.date_completed < timestamp:
            break
        print(transaction.date_completed)
        if search_note in transaction.note:
            print(f"USE THIS TRANSACTION DATE {transaction.date_completed}")
            donors[transaction.target.username] = transaction.amount
    return donors


def calc_progress_to_goal(donors):
    total = sum(donors.values())
    return total
