# Process the data received from LastFM API call

from .scrap_metadata import scrap_artist_art
from .scrap_metadata import scrap_cover_art


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


def get_data_from_track(track):
    """
    Returns relevant data from pylast.Track object
    :param track: pylast.Track object
    :return: dict of relevant data
    """
    data = {
        'name': track.get_name(),
        # 'duration': track.get_duration(),
        'artist': track.get_artist().get_name(),
        # 'image': track.get_cover_image(size=pylast.SIZE_MEDIUM),
        'playcount': track.get_playcount(),
    }
    data['image'] = scrap_cover_art(song=data['name'], artist=data['artist'])
    return data


def process_songs_data(tracks):
    """
    Accepts the raw list of songs returned by LastFM API, and returns list of processed data
    :param tracks: list(pylast.Track) received form the LastFM API call
    :return: list of dict containing processed data
    """

    processed_data = []

    for t in tracks:
        processed_data.append(get_data_from_track(t))

    return processed_data
