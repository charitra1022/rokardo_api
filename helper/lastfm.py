# functions that directly interact with the LastFM API

import pylast as lfm


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
    