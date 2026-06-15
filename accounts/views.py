from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, UserUpdateSerializer


@api_view(["POST"]) # 405 Method Not Allowed for GET, PUT, PATCH, DELETE
@permission_classes([permissions.AllowAny]) # Allow anyone to access the registration endpoint
def register(request):
	"""User registration endpoint."""
	serializer = RegisterSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.save()
	data = UserSerializer(user).data
	return Response(data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login(request):
	"""User login endpoint."""
	serializer = LoginSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.validated_data["user"]
	refresh = RefreshToken.for_user(user)
	return Response(
		{
			"access": str(refresh.access_token),
			"refresh": str(refresh),
			"user": UserSerializer(user).data,
		},
		status=status.HTTP_200_OK,
	)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
	"""User logout endpoint."""
	logout(request)
	return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
	"""User profile endpoint - retrieve, update, or delete user."""
	if request.method == "GET":
		user = request.user
		serializer = UserSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif request.method in ["PUT", "PATCH"]:
		user = request.user
		serializer = UserUpdateSerializer(user, data=request.data, partial=(request.method == "PATCH"))
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

	elif request.method == "DELETE":
		user = request.user
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
@api_view(["DELETE"])
@permission_classes([permissions.AllowAny])
def delete_all_users(request):
	"""Delete all users - for testing purposes only."""
	User.objects.all().delete()
	return Response({"detail": "All users deleted."}, status=status.HTTP_200_OK)