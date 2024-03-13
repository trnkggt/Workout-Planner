from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .serializers import CustomUserSerializer, RefreshTokenSerializer


class RegistrationView(GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh_token = RefreshToken.for_user(user)
        access_token = AccessToken.for_user(user)
        response_body = {
            "username": user.email,
            "access": str(access_token),
            "refresh": str(refresh_token)
        }

        return Response(response_body, status=status.HTTP_201_CREATED)




class UserLogOut(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"LOGOUT":"successful"},status=status.HTTP_204_NO_CONTENT)
