from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """
    Test API View
    """

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


class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request: HttpRequest):
        """
        Returns a hello message
        """

        a_viewset = [
            "Uses actions (list, create, retrieve, update and partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response(
            {
                "message": "Hello!",
                "a_viewset": a_viewset,
            }
        )

    def create(self, request: HttpRequest):
        """
        Create a hello message
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}!"
            return Response({"message": message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request: HttpRequest, pk=None):
        """
        Handle getting object by ID
        """

        return Response({"http_method": "GET"})

    def update(self, request: HttpRequest, pk=None):
        """
        Handle updating object
        """

        return Response({"http_method": "PUT"})

    def partial_update(self, request: HttpRequest, pk=None):
        """
        Handle updating part of object
        """

        return Response({"http_method": "PATCH"})

    def destroy(self, request: HttpRequest, pk=None):
        """
        Handle removing an object
        """

        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handle creating and updating profiles
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "email"]


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
