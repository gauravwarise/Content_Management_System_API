from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator, EmailValidator
from .models import User, ContentItem

from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[
        validate_password,
        RegexValidator(
            regex='^(?=.*[a-z])(?=.*[A-Z]).{8,}$',
            message='Password must be at least 8 characters long and contain at least one uppercase and one lowercase letter.'
        )
    ])

    email = serializers.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])

    phone = serializers.CharField(validators=[
        RegexValidator(
            regex='^\d{10}$',  
            message='Phone number must be 10 digits long.'
        )
    ])

    pincode = serializers.CharField(validators=[
        RegexValidator(
            regex='^\d{6}$',  
            message='Pincode should be 6 digits only.'
        )
    ])

    def validate_full_name(self, value):
        if len(value.split()) < 2:
            raise ValidationError("Both first name and last name are required.")
        return value


    class Meta:
        model = User
        fields = '__all__'




class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'