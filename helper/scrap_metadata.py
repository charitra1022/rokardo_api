# Functions to scrap metadata about songs, artists, etc.

# third-party imports
from bs4 import BeautifulSoup

# custom packages
from .request_handler import http_request


def scrap_artist_art(artist: str):
    """
    Scraps Google image search and returns image link for an artist accurately by artist name
    :param artist: Name of artist
    :return: Link to image of cover art
    """
    # example query string-> ed+sheeran
    query = f"{artist.replace(' ', '+')}"
    url = f"https://www.google.co.in/search?q={query}&hl=en&tbm=isch"

    # fetch the url data and convert to bs4 object
    r = http_request(url=url)
    soup = BeautifulSoup(r.content, 'html5lib')

    # get the body tag from response
    body = soup.find('body')

    # get all img tags
    image_tags = body.find_all('img')

    # images_src = []
    for image in image_tags:
        img_url = image.attrs.get("data-src")     # get the data-src attribute of the img tag
        if img_url is not None and 'http' in img_url:
            # images_src.append(x)
            # return a link that is valid openable image
            return img_url

    return ''
