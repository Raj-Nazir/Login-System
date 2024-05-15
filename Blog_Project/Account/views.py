from django import views
from django.shortcuts import render
from rest_framework.response import Response


from django.conf import settings

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver


from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.tokens import RefreshToken


from django.contrib.auth import authenticate, login, logout




from django.core.mail import send_mail

from django.conf import settings


from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


from rest_framework_simplejwt.authentication import JWTAuthentication




# Create your views here.

from rest_framework.decorators import api_view, APIView, action

from rest_framework import status, viewsets
from Account import serilizer


from Account.serilizer import  RegisterSerilizer, SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserProfileSerializer

from django.contrib.auth.models import User


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),  # type:ignore
    }




class Register(APIView):

    def post(self, request, format=None):
        serializer = RegisterSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)

        print("user:", user)
        print("token:", token)

        return Response(
            {"token": token, "msg": "Registration Successful"},
            status=status.HTTP_201_CREATED,
        )




class Login(APIView):

    def post(self, request, format=None):

        username = request.data.get("username")
        password = request.data.get("password")
        # email="raajnazir59181@gmail.com"
        # send_mail("send mail","Succesfully sended","settings.EMAIL_HOST_USER",[email])


        print("username", username, "password", password)

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            token = get_tokens_for_user(user)
            print(token)
            return Response(
                {"token": token, "msg": "Login Succesfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"errors": "Email or Password is not Valid"},
                status=status.HTTP_404_NOT_FOUND,
            )

        


class UserProfileView(APIView):
 
  authentication_classes=[JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    print('request.user',request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)







class UserChangePasswordView(APIView):
 
  authentication_classes=[JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    print( "from react", request.data)
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    
    
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)










class SendPasswordResetEmailView(APIView):
 

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Reset link send. Please check your Email"},
            status=status.HTTP_200_OK,
        )