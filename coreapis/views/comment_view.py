from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from coreapis.serializers.comments import CommentsSerializer
from coreapis.models.posts_model import Posts
from coreapis.models.comments_model import Comments


class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_post(self, post_id):
        try:
            return Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return None

    def post(self, request, post_id):
        post_instance = self.get_post(post_id=post_id)
        if not post_instance:
            return Response(
                {"res": "Post does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        data = {
            'comment': request.data.get('comment'),
            'post': post_id,
            'user': request.user.id
        }
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(
                {"Comment ID": obj.id,
                 "Comment": obj.comment},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
