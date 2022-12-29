from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from coreapis.models.posts_model import Posts
from coreapis.models.likes_model import Likes


class UnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_post(self, post_id):
        try:
            return Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return None

    def is_liked(self, post_id, user_id):
        try:
            return Likes.objects.filter(post=post_id, user=user_id)
        except Likes.DoesNotExist:
            return None

    def post(self, request, post_id):
        post_instance = self.get_post(post_id=post_id)
        if not post_instance:
            return Response(
                {"res": "Post does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        is_liked = self.is_liked(post_id=post_id, user_id=request.user.id)
        if not is_liked:
            return Response(
                {"res": "Given Post is not liked by you"},
                status=status.HTTP_400_BAD_REQUEST)
        is_liked.delete()
        return Response(
            {"res": "Post unlike successful"},
            status=status.HTTP_200_OK)
