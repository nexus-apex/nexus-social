from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import SocialAccount, ScheduledPost, Analytics
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusSocial with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexussocial.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if SocialAccount.objects.count() == 0:
            for i in range(10):
                SocialAccount.objects.create(
                    platform=random.choice(["facebook", "instagram", "twitter", "linkedin", "youtube"]),
                    username=f"Sample SocialAccount {i+1}",
                    followers=random.randint(1, 100),
                    status=random.choice(["connected", "disconnected", "paused"]),
                    profile_url=f"https://example.com/{i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 SocialAccount records created'))

        if ScheduledPost.objects.count() == 0:
            for i in range(10):
                ScheduledPost.objects.create(
                    title=f"Sample ScheduledPost {i+1}",
                    platform=f"Sample {i+1}",
                    content=f"Sample content for record {i+1}",
                    scheduled_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["draft", "scheduled", "published", "failed"]),
                    likes=random.randint(1, 100),
                    shares=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 ScheduledPost records created'))

        if Analytics.objects.count() == 0:
            for i in range(10):
                Analytics.objects.create(
                    platform=f"Sample {i+1}",
                    metric=f"Sample {i+1}",
                    period=random.choice(["daily", "weekly", "monthly"]),
                    value=round(random.uniform(1000, 50000), 2),
                    change_percent=round(random.uniform(1000, 50000), 2),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Analytics records created'))
