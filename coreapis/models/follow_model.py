from django.db import models
from authenticate.models import User


class Follow(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following_id = models.ForeignKey(User, on_delete=models.CASCADE)
