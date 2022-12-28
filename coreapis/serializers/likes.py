from rest_framework import serializers
from coreapis.models.likes_model import Likes


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ["post_id", "user_id"]
