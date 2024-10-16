from rest_framework import serializers

from accounts.models import User, Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already used.")
        return value

    def validate(self, attrs):
        if not attrs.get('password'):
            raise serializers.ValidationError("The password is required.")
        return attrs

    def create(self, validated_data):
        new_user = User(
            email=validated_data['email'],
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user


class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Попробуем найти пользователя по email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Проверка пароля
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password")

        # Если аутентификация прошла успешно, возвращаем пользователя
        attrs['user'] = user
        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class ProfileSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone', 'image']
