from users.serializers import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import SimpleJWTSerializer
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class SimpleJWTView(TokenObtainPairView):
    serializer_class = SimpleJWTSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()

        refresh_token = RefreshToken.for_user(user)

        return Response(
            {
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
            }, status=201
            )






