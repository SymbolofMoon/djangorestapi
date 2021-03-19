from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65, min_length=6, write_only=True)
    email=serializers.EmailField(max_length=255, min_length=4)
    first_name=serializers.CharField(max_length=255,min_length=2)
    last_name=serializers.CharField(max_length=255,min_length=2)
    username=serializers.CharField(max_length=255,min_length=2)


    class Meta:
        model=User
        fields=('username','first_name', 'last_name', 'email','password')

    def validate(self,attrs):

            email=attrs.get('email', '')
            if User.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError(
            {'email', ('Email is already in use')})


            return super().validate(attrs)


    def create(self, validated_data):
            user= User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()

            return user



