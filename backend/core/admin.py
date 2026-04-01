from django.contrib import admin
from .models import SocialAccount, ScheduledPost, Analytics

@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ["platform", "username", "followers", "status", "profile_url", "created_at"]
    list_filter = ["platform", "status"]
    search_fields = ["username"]

@admin.register(ScheduledPost)
class ScheduledPostAdmin(admin.ModelAdmin):
    list_display = ["title", "platform", "scheduled_date", "status", "likes", "created_at"]
    list_filter = ["status"]
    search_fields = ["title", "platform"]

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ["platform", "metric", "period", "value", "change_percent", "created_at"]
    list_filter = ["period"]
    search_fields = ["platform", "metric"]
