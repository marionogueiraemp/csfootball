from rest_framework import serializers
from .models import Team, PlayerApplication, TransferRequest
from users.models import CustomUser


class TeamSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    players = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.filter(is_player=True)
    )

    class Meta:
        model = Team
        fields = ['id', 'name', 'owner', 'owner_name', 'players', 'logo',
                  'description', 'created_at', 'matches_played', 'wins',
                  'draws', 'losses', 'goals_scored', 'goals_conceded',
                  'points', 'is_active', 'is_verified']
        read_only_fields = ['owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class PlayerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerApplication
        fields = ['id', 'player', 'team', 'status', 'created_at']


class TransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = ['id', 'player', 'from_team',
                  'to_team', 'status', 'created_at']
