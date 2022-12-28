from django.contrib import admin
from .models import (
    comments_model,
    likes_model,
    posts_model,
    follow_model
)

# Register your models here.
admin.site.register(comments_model.Comments)
admin.site.register(likes_model.Likes)
admin.site.register(posts_model.Posts)
admin.site.register(follow_model.Follow)
