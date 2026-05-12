from rest_framework import serializers
from .models import CustomUser, Team, Activity, Leaderboard, Workout

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='user', write_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'type', 'duration']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='user', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'points']
