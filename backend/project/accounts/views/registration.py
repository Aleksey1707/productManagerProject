from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import RegistrationSerializer


class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(request_body=RegistrationSerializer,
                         responses={status.HTTP_201_CREATED: "token"})
    def post(self, request, *args, **kwargs):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            dict(token=serializer.data.get('token', None)),
            status=status.HTTP_201_CREATED,
        )
