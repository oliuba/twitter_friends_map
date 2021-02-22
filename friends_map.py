"""
This module serves for map building.
"""

import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable
geolocator = Nominatim(user_agent='friends_map')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def place_to_coordinates(place: str) -> tuple:
    """
    Returns tuple with coordinates (latitude, longitude) of a place.
    >>> place_to_coordinates('Lviv')
    (49.841952, 24.0315921)
    >>> place_to_coordinates('New York')
    (40.7127281, -74.0060152)
    """
    try:
        location = geolocator.geocode(place)
        coordinates = location.latitude, location.longitude
    except (GeocoderUnavailable, AttributeError, ValueError):
        coordinates = None
    return coordinates


def coordinates_dct(locations_dct: dict) -> dict:
    """
    Returns a dictionary of users' screen names and coordinates.
    >>> coordinates_dct({'victoriya_roi': 'Vinnytsia, Ukraine', 'hannusiaa': 'Львів, Україна'})
    {'victoriya_roi': (49.2320162, 28.467975), 'hannusiaa': (49.841952, 24.0315921)}
    """
    coordinates_dict = dict()
    for screen_name in locations_dct:
        location = locations_dct[screen_name]
        coordinates = place_to_coordinates(location)
        if coordinates:
            coordinates_dict.update({screen_name: coordinates})
    return coordinates_dict


def twitter_friends_locations(locations: dict) -> folium.Map:
    """
    Returns a map with users' locations and their screen names on icons.
    """
    twitter_map = folium.Map()
    friends_locations = folium.FeatureGroup(name="Friends' locations")
    for friend in locations:
        friend_lat = locations[friend][0]
        friend_lon = locations[friend][1]
        friends_locations.add_child(folium.Marker(location=[friend_lat, friend_lon], \
            popup=friend, icon=folium.Icon(color='red')))
    twitter_map.add_child(friends_locations)
    return twitter_map
