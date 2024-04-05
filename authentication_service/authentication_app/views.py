from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializers, UserLoginSerializers, UserLogoutSerializer,TokenObtainPairView

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

#VIEWS FOR REGISTRATION
class UserRegistrationAPIView(APIView):
  def post(self, request):
   serializers = UserRegistrationSerializers(data = request.data)
   if serializers.is_valid():
     serializers.save()
     return Response(serializers.data, status = status.HTTP_201_CREATED)
   return Response(serializers.error, status = status.hTTP_400_BAD_REQUEST)

#VIEWS FOR LOGIN 
class UserLoginAPIView(APIView):
  def post(self, request):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = serializer.validated_data['tokens']
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#VIEWS FOR LOGOUT
class UserLogoutAPIView(APIView):
  def post(self, request):
      serializer = UserLogoutSerializer(data=request.data)
      if serializer.is_valid():
          serializer.logout(serializer.validated_data)
          return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#For token generation
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = serializer.validated_data
            # Customize response data if needed
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)