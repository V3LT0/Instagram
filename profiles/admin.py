from django.contrib import admin

from profiles.models import UserProfiles, Follow

@admin.register(UserProfiles)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user","birth_date"]

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ["follower", "following", "created_at"]