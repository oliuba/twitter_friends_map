"""
This is the main module of the programm. It works with Flask and creates a web page
that asks a user to enter his/her twitter account screenname and a bearer token
and shows them a web map of their friends' locations.
"""

from flask import Flask, render_template, request
from twitter_api_analysis import get_twitter_info, get_locations
from friends_map import coordinates_dct, twitter_friends_locations

app = Flask(__name__)

@app.route("/")
def index():
    """
    Returns the main page that contains the fields to enter twitter screenname and bearer token.
    """
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    """
    The main function that returns a web page with a friends map
    or a failure page if the forms are empty.
    """
    if not request.form.get("name") or not request.form.get("bearer token"):
        return render_template("failure.html")
    name = request.form.get("name")
    bearer_token = request.form.get("bearer token")
    try:
        users_data = get_twitter_info(name, bearer_token)
        friends_locations = get_locations(users_data)
        friends_coordinates = coordinates_dct(friends_locations)
        twitter_friends_map = twitter_friends_locations(friends_coordinates)
        twitter_friends_map.save(f'templates/{name}_friends_map.html')
    except KeyError:
        return render_template("failure.html")
    return render_template(f'{name}_friends_map.html')

app.run()
