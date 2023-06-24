from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request: HttpRequest, format=None):
        """
        Returns a list of API View features
        """
        an_apiview = [
            "Uses HTTP methods as functions",
            "Is similar to traditional Django view",
            "Gives you the most control over the application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello", "an_apiview": an_apiview})

    def post(self, request: HttpRequest):
        """
        Create a hello message with our name
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: HttpRequest, pk=None):
        """
        Handle updating an object
        """
        return Response({"method": "PUT"})

    def patch(self, request: HttpRequest, pk=None):
        """
        Handle partial update of an object
        """
        return Response({"method": "PATCH"})

    def delete(self, request: HttpRequest, pk=None):
        """
        Delete an object
        """
        return Response({"method": "DELETE"})
