from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'is_player',
                  'avatar', 'bio', 'goals_scored', 'assists',
                  'yellow_cards', 'red_cards', 'matches_played']
        read_only_fields = ['role']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_player']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
