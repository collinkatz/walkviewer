from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import os
# Create your views here.

def dump_file_contents(filename):
    with open(filename, 'r') as file:
        return file.read().rstrip()

"""
APIView for quering the server for the maps API key
"""
class mapsApiKey(APIView):

    def get(self, request):
        print(settings.MAPS_API_KEY_LOCATION)
        if os.path.isfile(settings.MAPS_API_KEY_LOCATION):
            return Response(dump_file_contents(settings.MAPS_API_KEY_LOCATION), status=200)
        else:
            print("Need to reconfigure maps API key")
            return Response("No maps api key set", status=500)