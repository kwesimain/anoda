from rest_framework import serializers
from .models import Userprofile, VerificationStatus, VerificationRq,  SteezeLikes, SteezeCom, Steeze, RelationRq,  OrganizersRq, OrgStatus, Messages, Flags, FlagRequest, Event, Chatroom, Comment, Chatmembership

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'

class ChatmembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatmembership
        fields = '__all__'

class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class FlagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flags
        fields = '__all__'

class FlagRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlagRequest
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class OrgStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgStatus
        fields = '__all__'

class OrganizersRqSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizersRq
        fields = '__all__'

class RelationRqSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationRq
        fields = '__all__'

class SteezeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steeze
        fields = '__all__'

class SteezeComSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteezeCom
        fields = '__all__'

class SteezeLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteezeLikes
        fields = '__all__'

class VerificationRqSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationRq
        fields = '__all__'

class VerificationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationStatus
        fields = '__all__'