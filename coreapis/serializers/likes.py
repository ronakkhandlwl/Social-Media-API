from rest_framework import serializers
from coreapis.models.likes_model import Likes


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ["post", "user"]
