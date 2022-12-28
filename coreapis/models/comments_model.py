from django.db import models
from authenticate.models import User
from .posts_model import Posts


class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
