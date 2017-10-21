from django.contrib.auth import get_user_model
from django.db.models import  Q
from rest_framework import serializers
from rest_framework.serializers import(
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    CharField,
)

''' User = get_user_model() '''
from .models import User

class UserLoginSerializer(ModelSerializer):
    first_name = CharField(read_only=True)
    last_name = CharField(read_only=True)
    email = EmailField(read_only=True)
    username = CharField()
    password = serializers.CharField(
    style={'input_type': 'password'}
)

    class Meta:
        model = User
        fields = [
            
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            
            
        ]

    def validate(self, data):
       
        user_obj = None
        username = data.get("username",None)
        password = data['password']
        if  not username:
            raise ValidationError("A username or email is required to login")
        user = User.objects.filter(
            username=username 
           
        ).distinct()

        if  user.count() ==1:
            user_obj = user.first()
            if user_obj.password == password:
                data['email']=user_obj.email
                data['first_name']=user_obj.first_name
                data['last_name']=user_obj.last_name
                
            else:
                raise ValidationError("Unable to log in with provided credentials.")
        else:
            raise ValidationError("Unable to log in with provided credentials.")
            
        
 
        
        return data