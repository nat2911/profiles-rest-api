from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
