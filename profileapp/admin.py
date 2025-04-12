from django.contrib import admin
from profileapp.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(Profile, ProfileAdmin)