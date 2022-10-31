from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from helper.lastfm import get_track_list_by_search
from helper.lastfm_processor import process_songs_data


class SearchSong(APIView):
    def get(self, request):
        """
        Searches for a song by its name, and returns list of matching songs from API
        :param request:
        :return: DRF Response containing song list
        """

        query = request.GET.get('q').lower()  # get the search string
        data = process_songs_data(get_track_list_by_search(query))

        print(data)

        return Response(data, status=status.HTTP_302_FOUND)
