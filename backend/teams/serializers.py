from rest_framework import serializers
from competitions.serializers import CompetitionSerializer
from .models import PlayerApplication, Team, TransferRequest


class TeamSerializer(serializers.ModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'logo', 'owner', 'players']
        read_only_fields = ['owner', 'players']

    def create(self, validated_data):
        # Set the owner of the team as the current user
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class PlayerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerApplication
        fields = ['id', 'player', 'team', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']


class TransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = ['id', 'player', 'from_team',
                  'to_team', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
