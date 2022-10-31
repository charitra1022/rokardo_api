# Process the data received from LastFM API call

from .scrap_metadata import scrap_artist_art


def get_data_from_artist(artist):
    """
    Returns relevant data from pylast.Artist object
    :param artist: pylast.Artist object
    :return: dict of relevant data
    """
    data = {
        "name": artist.get_name(),
        "plays": artist.get_playcount(),
        "mbid": artist.get_mbid(),
        "bio": artist.get_bio_summary(),
    }
    data["image"] = scrap_artist_art(data["name"])
    return data


def process_artists_data(topItems):
    """
    Accepts the list of raw data returned by the LastFM API, and returns list of processed data
    :param topItems: list(TopItem) received from the LastFM API call
    :return: list of dict containing processed data
    """

    processed_data = []

    for i in topItems:
        processed_data.append(get_data_from_artist(i.item))

    return processed_data
