from unittest.mock import patch

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route


class SimpleAPI(APIView):
    def get(self, request, format=None):
        return Response({"error": False})

    @detail_route(methods=["GET"])
    def details(self, request, pk=None):
        return Response({"ok": True})

    @list_route(methods=["LIST"])
    def listing(self, request):
        return Response({"data": []})


@patch("os")
def other_decorator(self, os_mock):
    pass
