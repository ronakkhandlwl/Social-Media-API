from rest_framework import serializers
from coreapis.models.comments_model import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["comment", "post", "user"]
