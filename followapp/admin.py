from django.contrib import admin
from followapp.models import Follow


class FollowAdmin(admin.ModelAdmin):
    model = Follow


admin.site.register(Follow, FollowAdmin)