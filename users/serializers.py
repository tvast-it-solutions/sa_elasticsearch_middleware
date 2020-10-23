from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

User = get_user_model()
UserType = ['Admin', 'Analyst']

class CustomRegisterSerializer(RegisterSerializer):
    userType = serializers.CharField(max_length=50, required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['userType'] = self.validated_data.get('userType', '')
        if str(data_dict['userType']) in UserType:
            return data_dict
        else:
            raise serializers.ValidationError('Usertype is not defined correctly')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('userType', 'username', 'password')
        
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass
