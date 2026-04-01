from django.db import models

class SocialAccount(models.Model):
    platform = models.CharField(max_length=50, choices=[("facebook", "Facebook"), ("instagram", "Instagram"), ("twitter", "Twitter"), ("linkedin", "LinkedIn"), ("youtube", "YouTube")], default="facebook")
    username = models.CharField(max_length=255, blank=True, default="")
    followers = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("connected", "Connected"), ("disconnected", "Disconnected"), ("paused", "Paused")], default="connected")
    profile_url = models.URLField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.platform

class ScheduledPost(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    scheduled_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("scheduled", "Scheduled"), ("published", "Published"), ("failed", "Failed")], default="draft")
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Analytics(models.Model):
    platform = models.CharField(max_length=255)
    metric = models.CharField(max_length=255, blank=True, default="")
    period = models.CharField(max_length=50, choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")], default="daily")
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    change_percent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.platform
