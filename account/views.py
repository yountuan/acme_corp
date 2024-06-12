from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'message': 'Successfully registered', 'activation_code': user.activation_code}, status=status.HTTP_201_CREATED)

class ActivationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('User does not exist', status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Successfully activated', status=status.HTTP_200_OK)

class DeleteAccountView(APIView):
    def delete(self, request, email):
        try:
            user = User.objects.get(email=email)
            user.delete()
            return Response('Account successfully deleted', status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)

class ObtainActivationCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'activation_code': user.activation_code}, status=status.HTTP_200_OK)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
