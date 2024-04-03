from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


#SERIALIZERS FOR REGISTRATION 
class UserRegistrationSerializers(serializers.ModelSerializer):
  password = serializers.CharField(write_only =True)
  
  class Meta:
    model =CustomUser
    fields= "__all__"
  
  
  def create(self, validate_data):
    user = CustomUser.objects.create(
      email = validate_data['email'],
      password = validate_data['password'],
      username = validate_data['username'], 
     )
    return user
  

#SERIALIZERS FOR LOGIN 
class UserLoginSerializers(serializers.Serializer):
  email = serializers.EmailField(max_length = 100)
  password = serializers.CharField(max_length= 100)
  
  def validate(self, attrs):
      email = attrs.get('email')
      password = attrs.get('password')
      user = authenticate(email=email, password=password)

      if not user:
          raise serializers.ValidationError('Invalid email or password')

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