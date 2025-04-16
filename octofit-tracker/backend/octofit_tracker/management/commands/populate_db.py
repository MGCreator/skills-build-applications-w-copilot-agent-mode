from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(username="john_doe", email="john@example.com", password="password123")
        user2 = User.objects.create(username="jane_doe", email="jane@example.com", password="password123")

        # Create Teams
        team1 = Team.objects.create(name="Team Alpha")
        team1.members.add(user1, user2)

        # Create Activities
        Activity.objects.create(user=user1, activity_type="Running", duration=timedelta(minutes=45))
        Activity.objects.create(user=user2, activity_type="Cycling", duration=timedelta(minutes=75))

        # Create Leaderboard Entries
        Leaderboard.objects.create(user=user1, score=150)
        Leaderboard.objects.create(user=user2, score=200)

        # Create Workouts
        Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        Workout.objects.create(name="Sit-ups", description="Do 30 sit-ups")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
