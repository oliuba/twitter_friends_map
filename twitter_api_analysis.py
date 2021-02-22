"""
This module works with Twitter API and gets user's friends' locations.
"""

import requests

def get_twitter_info(screen_name: str, bearer_token: str) -> dict:
    """
    Returns a dictionary with a user's twitter actions and other data.
    """
    base_url = 'https://api.twitter.com/'
    search_url = f'{base_url}1.1/friends/list.json'
    search_headers = {'Authorization': f'Bearer {bearer_token}'}
    search_params = {'screen_name': screen_name, 'count': 200}
    response = requests.get(search_url, headers=search_headers, params=search_params)
    json_response = response.json()
    return json_response


def get_locations(twitter_data: dict) -> dict:
    """
    Returns a dictionary where keys are users' accounts and the values are their locations.
    """
    locations_dct = dict()
    for user in twitter_data['users']:
        if user['location']:
            locations_dct.update({user['screen_name']: user['location']})
    return locations_dct
