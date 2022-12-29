from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from coreapis.serializers.posts import PostsSerializer
from coreapis.models.posts_model import Posts
from coreapis.models.likes_model import Likes
from coreapis.models.comments_model import Comments


class PostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_post(self, post_id):
        try:
            return Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return None

    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'user': request.user.id
        }
        serializer = PostsSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(
                {"Post ID": obj.id,
                 "Title": obj.title,
                 "Description": obj.description,
                 "Created At": obj.created_at},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post_instance = self.get_post(post_id=post_id)
        if not post_instance:
            return Response(
                {"res": "Post does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        post_instance.delete()
        return Response(
            {"res": "Post successfully deleted"},
            status=status.HTTP_200_OK)

    def get(self, request, post_id):
        post_instance = self.get_post(post_id=post_id)
        if not post_instance:
            return Response(
                {"res": "Post does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        obj = Posts.objects.get(id=post_id)
        title = obj.title
        desc = obj.description
        likes = Likes.objects.filter(post=post_id).count()
        comments = list(Comments.objects.filter(post=post_id).values_list('comment', flat=True))
        if not likes:
            likes = 0
        if not comments:
            comments = []
        return Response({
            "Title": title,
            "Description": desc,
            "Likes": likes,
            "Comments": comments},
            status=status.HTTP_200_OK)
