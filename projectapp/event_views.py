from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Events
from .serializers import EventsSerializer
from rest_framework.authentication import TokenAuthentication  # Token-based authentication

class EventsListCreateView(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the organizer as the currently authenticated user
        serializer.save(organizer=self.request.user)

class EventsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# Define more views for other functionalities...
