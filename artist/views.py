from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from helper.lastfm_processor import process_top_artists_data

from helper.lastfm import get_top_artists


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
