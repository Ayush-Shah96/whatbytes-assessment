from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer


class RegisterView(APIView):
    """
    POST /api/auth/register/
    Register a new user with name, email, and password.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = serializer.save()
        
        # Generate JWT tokens for the newly registered user
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "success": True,
                "message": "User registered successfully.",
                "user": UserSerializer(user).data,
                "tokens": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                }
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(TokenObtainPairView):
    """
    POST /api/auth/login/
    Log in a user and return JWT tokens.
    Accepts email and password.
    """
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        data = serializer.validated_data
        user = serializer.user
        
        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "user": UserSerializer(user).data,
                "tokens": {
                    "access": data["access"],
                    "refresh": data["refresh"],
                }
            },
            status=status.HTTP_200_OK
        )
