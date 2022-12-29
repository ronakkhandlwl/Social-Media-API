from rest_framework import serializers
from coreapis.models.follow_model import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["follower", "following"]
