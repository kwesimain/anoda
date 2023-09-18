from rest_framework import generics, status, permissions
from ..models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer  # Use your custom user profile serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class UserRegistrationView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer  # Use your custom serializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to register

    def perform_create(self, serializer):
        # Customize user creation logic if needed
        serializer.save()

# You can create more views for user profile management as needed.
class UserLoginView(ObtainAuthToken):
    """Custom login view to generate authentication token."""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class FollowUserView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer  # Use your custom user profile serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_to_follow = self.get_object()
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Implement logic to follow the user
        request.user.profile.following.add(user_to_follow)
        return Response(status=status.HTTP_200_OK)
    
class UnfollowUserView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer  # Use your custom user profile serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_to_unfollow = self.get_object()

        # Check if the user is already followed
        if user_to_unfollow in request.user.profile.following.all():
            # Unfollow the user
            request.user.profile.following.remove(user_to_unfollow)
            return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": f"You are not following {user_to_unfollow.username}."}, status=status.HTTP_400_BAD_REQUEST)
        

class ListFollowersView(generics.ListAPIView):
    serializer_class = UserProfileSerializer  # Use your custom user profile serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.followers.all()

class ListFollowingView(generics.ListAPIView):
    serializer_class = UserProfileSerializer  # Use your custom user profile serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.following.all()