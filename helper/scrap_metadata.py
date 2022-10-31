# Functions to scrap metadata about songs, artists, etc.

# third-party imports
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch

# custom packages
from .request_handler import http_request


def _scrap_first_image(url: str):
    """
    Scraps Google image search and returns first image link for desired search terms
    :param url: Link to scrap
    :return: link to image
    """

    # fetch the url data and convert to bs4 object
    r = http_request(url=url)
    soup = BeautifulSoup(r.content, 'html5lib')

    # get the body tag from response
    body = soup.find('body')

    # get all img tags
    image_tags = body.find_all('img')

    # images_src = []
    for image in image_tags:
        img_url = image.attrs.get("data-src")  # get the data-src attribute of the img tag
        if img_url is not None and 'http' in img_url:
            # images_src.append(x)
            # return a link that is valid openable image
            return img_url

    return ''


def scrap_artist_art(artist: str):
    """
    Scraps Google image search and returns image link for an artist accurately by artist name
    :param artist: Name of artist
    :return: Link to image of cover art
    """
    # example query string-> ed+sheeran
    query = f"{artist.replace(' ', '+')}"
    url = f"https://www.google.co.in/search?q={query}&hl=en&tbm=isch"
    return _scrap_first_image(url)


def scrap_cover_art(song: str, artist: str):
    """
    Scraps Google image search and returns image link for a song accurately based on song name and artist name
    :param song: Name of song
    :param artist: Name of artist
    :return: Link to image of cover art
    """
    # example query string-> shape+of+you+ed+sheeran+cover+art
    query = f"{song.replace(' ', '+')}+{artist.replace(' ', '+')}+cover+art"
    url = f"https://www.google.co.in/search?q={query}&hl=en&tbm=isch"
    return _scrap_first_image(url)


def get_youtubelink_from_song_artist(song, artist):
    """
    Retrieves YouTube link for a song accurately by searching by song name and artist name
    :param song: Name of song
    :param artist: Name of artist
    :return: Link to YouTube link for the video
    """

    # get search results from YouTube using song name and artist
    search_results = YoutubeSearch(f"{song} {artist}", max_results=2).to_dict()
    videoID = search_results[0]['id']

    # Links for YouTube video
    youtube_player = 'https://www.youtube-nocookie.com/embed/{id}?autoplay=1&controls=0&disablekb=1&enablejsapi=1&iv_load_policy=3&vq=low'
    youtube_player = 'https://www.youtube.com/embed/{id}'
    youtube_player = 'https://www.youtube.com/v/VIDEO_ID?playlist=VIDEO_ID&autoplay=1&rel=0'
    youtube_player = 'https://www.youtube.com/watch?v={id}'

    # Get required data from the result dict
    # data = {
    #     'name': search_results[0]['title'],
    #     'link': youtube_player.format(id=search_results[0]['id'])
    # }

    return youtube_player.format(id=videoID)
