from django.contrib.auth.models import User
from django.db import models


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    other = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        unique_together = ('user', 'other')
