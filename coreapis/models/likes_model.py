from django.db import models
from authenticate.models import User
from .posts_model import Posts


class Likes(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
