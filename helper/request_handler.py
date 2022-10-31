# Request related functions

import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
}


def http_request(url, params=None):
    """
    Fetchs url with defined params using requests module and returns response
    :param url: URl of page to fetch
    :param params:
    :return: Response object
    """

    if params is not None:
        response = requests.get(url, headers=headers, params=params)
    else:
        response = requests.get(url, headers=headers)
    return response
