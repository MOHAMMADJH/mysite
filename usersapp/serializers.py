from asyncore import read
from rest_framework import serializers
from .models import note
from rest_framework import serializers
from django.contrib.auth import get_user_model

from djoser.serializers import UserCreateSerializer



"""
Serializers for the user API View.
"""



from django.contrib.auth import (
    get_user_model,
    authenticate,
)


from django.utils.translation import gettext as _

from rest_framework import serializers




class NoteSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = note
        fields = ["user",'note', 'email', 'password', 'self_d', 'note_name', 'note_id']
        # fields = '__all__'
        read_only_fields = ['pk']

    # def get_validation_exclusions(self):
    #         exclusions = super(note, self).get_validation_exclusions()
    #         return exclusions + ['owner']



    """
    
    [
    {
        "note": "sadasd",
        "email": "mohjas97_fes@hotmail.com",
        "password": "1233456",
        "self_d": "2022-07-23T17:27:06Z",
        "note_name": "asd",
        "note_id": "9613237a-c503-4e13-b279-84b5c18fe95f"
    },
    
    
    """






#######################################################################################




class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['id','email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs



        ###################################################################################


### JWT 

User = get_user_model()

class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'name']

    # def get_full_name(self, obj):
    #     return f'{obj.first_name} {obj.last_name}'


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Model Serializer that serializes data from the registeration route
    confirm_password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "name",


            "password",
            "confirm_password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):

        email = self.validated_data["email"]
        name = self.validated_data["name"]
        new_user = User(
            email=email,
            name=name,

        )

        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Passwords must match"}, code="authorization"
            )  # checks to validate password inputed by client
        else:
            new_user.set_password(password)
            new_user.save()
            return new_user

