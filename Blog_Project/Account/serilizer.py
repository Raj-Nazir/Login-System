
from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.core.validators import validate_email



from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator





class RegisterSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username', 'password', 'email', 'first_name', 'last_name']
        
        # exclude=['last_login',"is_superuser", 'is_staff', 'is_active','date_joined','id']
      
      
    @staticmethod
    def validate_password(password:str)->str:
        return make_password(password)
   
       
    def validate(self, data):
        username = data.get('username')
        first_name = data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        password=data.get('password')
        
        print(f"username{username} and last_name{last_name}")
        
        if len(username)<3:
            raise serializers.ValidationError({'username_error':'Please enter a valid username must be at least 3 characters'})
        
        if len(first_name)<3:
            raise serializers.ValidationError({'first_name_error':'Please enter a valid first_name'})
        
        if len(last_name)<3:
            raise serializers.ValidationError({'last_name_error':'Please enter a valid last_name'})
        
        if  validate_email(email):
            raise serializers.ValidationError({'email_error':'Please enter a valid email'})
        
        if len(password)<5:
            raise serializers.ValidationError({'password_error':'Please enter a password must be Greater than 5'})
        
        return data
       
       
   






class UserProfileSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model=User
        fields=['id','first_name', 'email']
        
       
      
       
 
      
class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
#   password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', ]

  def validate(self, attrs):
    password = attrs.get('password')
    # password2 = attrs.get('password2')
    user = self.context.get('user')
    
    print("reset User:",user)
    if password is None:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password) # type:ignore
    user.save() # type:ignore
    return attrs






class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    fields = ['email']

  def validate(self, attrs):
    email = attrs.get('email')
    if User.objects.filter(email=email).exists():
      user = User.objects.get(email = email)
      uid = urlsafe_base64_encode(force_bytes(user.id))
      print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(user)
      print('Password Reset Token', token)
      link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
      print('Password Reset Link', link)
      # Send EMail
      body = 'Click Following Link to Reset Your Password '+link
      data = {
        'subject':'Reset Your Password',
        'body':body,
        'to_email':user.email
      }
      # Util.send_email(data)
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')