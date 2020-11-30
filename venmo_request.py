from venmo_api import Client, AuthenticationApi, ApiClient
import datetime


def find_user_for_request(username, access_token):
    '''
    Searches for a user given a username and an access token.
    Returns the user found id. If no user is found, returns false.
    '''
    venmo = Client(access_token=access_token)
    users = venmo.user.search_for_users(query=username,
                                        page=1)
    for found_user in users:
        if found_user.username == username:
            return found_user.id
    return False


def request_friend(user_id, min_amount, access_token, note):
    '''
    Requests a venmo user by their user id,
    requests them the post's minimum donation amount,
    uses the Post's access token to request,
    and attaches a note with the Post's title in it.
    '''
    venmo = Client(access_token=access_token)
    venmo.payment.request_money(
        min_amount, f"{note} - Create your own Venmo crowdfund with Crowdmo.io", user_id)


def venmo_get_otp(username, password, device_id):
    '''
    Creates an one time password
    given a username, password, 
    and a randomly generated device id
    '''
    return Client.get_access_token(username=username, password=password, device_id=device_id)


def venmo_get_access_token(otp_secret, otp_code, device_id):
    '''
    Returns the user's access token given
    the otp secret, the user's inputed otp code
    and the randomly generated device id.
    '''
    authn_api = AuthenticationApi(api_client=ApiClient(), device_id=device_id)
    return authn_api.authenticate_using_otp(user_otp=otp_code, otp_secret=otp_secret)


def update_contributors(search_note, creation_date, access_token):
    '''
    Returns a dictionary with username:donation pairs.
    Searches through a user's transaction data up until the
    creation date of the post.

    Looks at each transaction and checks if the post's
    unique transaction note is inside of the transcation note.
    If so, the username and donation amount are added to the donors
    dictionary.
    '''
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
    '''
    Sums the total donations a post has and returns the value.
    '''
    total = sum(donors.values())
    return total
