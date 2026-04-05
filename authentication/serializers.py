from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT serializer that accepts email instead of username."""
    
    username_field = 'email'

    def validate(self, attrs):
        # Map email to username for authentication
        email = attrs.get('email', '')
        try:
            user = User.objects.get(email=email.lower())
            attrs[self.username_field] = user.username
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "No account found with this email address."}
            )
        return super().validate(attrs)
