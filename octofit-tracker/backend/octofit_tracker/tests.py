from django.test import TestCase
from .models import Team, CustomUser, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_str(self):
        self.assertIn('testuser', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_leaderboard_str(self):
        self.assertIn('testuser', str(self.leaderboard))
