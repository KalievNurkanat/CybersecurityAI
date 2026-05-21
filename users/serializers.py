from rest_framework import serializers
from users.models import CustomUser
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SimpleJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = str(user.email)

        return token
    
 
class GoogleCodeSerilizer(serializers.Serializer):
    code = serializers.CharField()


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()


class UserRegisterSerializer(UserBaseSerializer):
    def validate_username(self, username):
        if CustomUser.objects.filter(username=username).exists():
           raise ValidationError("Such a username already exists")
        return username
    
    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
           raise ValidationError("Such an email already exists")
        return email
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"]
        )

        return user

