# Process the data received from LastFM API call

from .scrap_metadata import scrap_artist_art


def process_artists_data(artists):
    """
    Accepts the raw data returned by the LastFM API, and returns list of processed data
    :param artists: list(TopItem) received from the LastFM API call
    :return: list of dict containing processed data
    """

    processed_data = []

    for a in artists:
        artist = {
            "name": a.item.get_name(),
            "plays": a.item.get_playcount(),
            "mbid": a.item.get_mbid(),
            "bio": a.item.get_bio_summary(),
        }
        artist["image"] = scrap_artist_art(artist["name"])
        processed_data.append(artist)

    return processed_data
