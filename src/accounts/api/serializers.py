from rest_framework import serializers

from accounts.models import User, Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        new_user = User(
            username=validated_data['username'],
        )

        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone', 'image']
