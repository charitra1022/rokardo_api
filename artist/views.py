from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from helper.lastfm_processor import process_top_artists_data, process_top_tracks_data
from helper.lastfm_processor import get_data_from_artist

from helper.lastfm import get_top_artists, get_artist_top_albums
from helper.lastfm import get_artist_by_mbid


class GetTopArtists(APIView):
    """
    Returns API Response for top played artists
    """

    def get(self, request):
        """
        Gets list of top artists
        :param request:
        :return: DRF Response containing artist list
        """

        artists = process_top_artists_data(get_top_artists(limit=5))
        return Response(artists, status=status.HTTP_302_FOUND)


class GetArtistByMbid(APIView):
    """
    Returns API Response for top played artists
    """

    def get(self, request):
        """
        Gets list of top artists
        :param request:
        :return: DRF Response containing artist list
        """

        mbid = request.GET.get("artist_mbid")

        artist = get_artist_by_mbid(mbid)   # pylast.Artist object from mbid
        artist_data = get_data_from_artist(artist)  # artist data
        top_albums = process_top_tracks_data(get_artist_top_albums(artist))  # top played albums of the artist

        data = {
            'details': artist_data,
            'top_tracks': top_albums,
        }

        return Response(data, status=status.HTTP_302_FOUND)


