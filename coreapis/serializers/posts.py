from pdb import post_mortem
from rest_framework import serializers
from coreapis.models.posts_model import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["title", "description", "user"]
