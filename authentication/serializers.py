from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    name = serializers.CharField(required=True, max_length=150)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'password_confirm')
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate_email(self, value):
        """Ensure email is unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value.lower()

    def validate(self, attrs):
        """Validate that both passwords match."""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        """Create and return a new user."""
        name = validated_data.pop('name')
        validated_data.pop('password_confirm')
        
        # Split name into first/last name
        name_parts = name.strip().split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''

        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name,
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """Serializer for displaying user info."""
    
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email')

    def get_name(self, obj):
        return obj.get_full_name() or obj.username


class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email', '').lower()
        password = attrs.get('password', '')

        # Find user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "No account found with this email address."}
            )

        # Authenticate using their username + password
        authenticated_user = authenticate(
            request=self.context.get('request'),
            username=user.username,
            password=password
        )

        if not authenticated_user:
            raise serializers.ValidationError(
                {"detail": "Incorrect password."}
            )

        if not authenticated_user.is_active:
            raise serializers.ValidationError(
                {"detail": "This account is inactive."}
            )

        # Generate tokens manually
        refresh = RefreshToken.for_user(authenticated_user)

        self.user = authenticated_user

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }