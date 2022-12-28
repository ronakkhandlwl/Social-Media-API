from django.db import models
from authenticate.models import User
from .posts_model import Posts


class Comments(models.Model):
    comment = models.TextField()
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
