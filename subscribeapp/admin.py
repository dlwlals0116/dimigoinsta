from django.contrib import admin
from subscribeapp.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription


admin.site.register(Subscription, SubscriptionAdmin)