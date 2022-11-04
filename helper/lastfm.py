# functions that directly interact with the LastFM API

import pylast as lfm
from helper.request_handler import http_request


def initialize_lastfm():
    """
    Creates and returns LastFM Network object that can be used to interact with LastFM API
    :return:
    """
    API_KEY = "ae89906ded7c87b6ad664f9c1ca5e8a8"
    SECRET_KEY = "f4ca006521ada4aeb85d9dcc317f9be6"

    network = lfm.LastFMNetwork(
        api_key=API_KEY,
        api_secret=SECRET_KEY,
    )

    return network


def get_top_artists(limit=10):
    """
    Returns a list of top artists streaming on LastFM
    :param limit: Number of artists to return. Default 10
    :return: list of pylast.TopItem(pylast.Artist) object
    """

    network = initialize_lastfm()
    artists = network.get_top_artists(limit=limit)
    return artists


# def get_track_list_by_search(query):
#     """
#     Searches for a song and returns list of matching tracks
#     :param query: Song name query
#     :return: list(pylast.Track)
#     """
#
#     network = initialize_lastfm()
#     songs = network.search_for_track(artist_name='', track_name=query).get_next_page()
#     return songs


def get_track_list_by_search(query, limit=5):
    """
    Searches for a song and returns list of matching tracks
    :param limit: Number of results per request
    :param query: Song name query
    :return: response from API
    """

    API_URL = 'http://ws.audioscrobbler.com/2.0'
    params = {
        'method': 'track.search',
        'track': query,
        'limit': limit,
        'page': 1,
        'api_key': 'ae89906ded7c87b6ad664f9c1ca5e8a8',
        'format': 'json'
    }

    return http_request(url=API_URL, params=params)


def get_artist_by_mbid(mbid: str):
    """
    Returns pylast.Artist object by artist mbid
    :param mbid: mbid of the Artist to be searched
    :return: pylast.Artist object with respective mbid
    """
    network = initialize_lastfm()
    artist = network.get_artist_by_mbid(mbid)
    return artist
