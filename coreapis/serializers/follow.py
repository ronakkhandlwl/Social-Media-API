from rest_framework import serializers
from coreapis.models.follow_model import Follow


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["follower_id", "following_id"]
