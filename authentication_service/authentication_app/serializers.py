from multiprocessing import AuthenticationError
from .models import CustomUser

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password


#SERIALIZERS FOR REGISTRATION 
class UserRegistrationSerializers(serializers.ModelSerializer):
  password = serializers.CharField(write_only =True)
  
  class Meta:
    model =CustomUser
    fields= "__all__"
  
  
  def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user
  

#SERIALIZERS FOR LOGIN 
class UserLoginSerializers(serializers.Serializer):
  email = serializers.EmailField(max_length = 100)
  password = serializers.CharField(max_length= 100)
  
  # class Meta:
  #   model =CustomUser
  #   fields= "__all__"
  
  
  def validate(self, attrs):
      email = attrs.get('email')
      password = attrs.get('password')
      
      # user = authenticate(email=email, password=password)
      user = get_object_or_404(CustomUser, email = email)
      print(user)
      
      if not user:
          # print(serializers.errors)
          raise serializers.ValidationError('Invalid email or password')
        
      
      if check_password(password, user.password):
        
        refresh = RefreshToken.for_user(user)
        attrs['user'] = user
        attrs['tokens'] = {'refresh': str(refresh), 'access': str(refresh.access_token)}

      return attrs
    
#SERIALIZERS FOR LOGOUT

class UserLogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            
        except Exception as e:
            raise serializers.ValidationError('Unable to logout')

        return attrs
      

from django.contrib.auth.models import User
#Serializer for token generation
class CustomTokenObtainPairSerializer(TokenObtainPairView):
    default_error_messages = {
        'no_active_account': 'No active account found with the given credentials'
    }

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if not user.is_active:
            raise serializers.ValidationError(
                self.error_messages['no_active_account'],
                code='no_active_account'
            )
        return data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
