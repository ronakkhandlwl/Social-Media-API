from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from coreapis.models.posts_model import Posts
from coreapis.models.likes_model import Likes
from coreapis.models.comments_model import Comments
from authenticate.models import User


class AllPostsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        post_obj = list(Posts.objects.filter(user_id=user_id).values_list('id', flat=True))
        post_list = []
        for post_id in post_obj:
            obj = Posts.objects.get(id=post_id)
            title = obj.title
            desc = obj.description
            created_at = obj.created_at
            likes = Likes.objects.filter(post=post_id).count()
            comments = list(Comments.objects.filter(post=post_id).values_list('comment', flat=True))
            post_list.append({
                "id": post_id,
                "title": title,
                "desc": desc,
                "created_at": created_at,
                "likes": likes,
                "comments": comments
            })
        return Response(
            {"res": post_list},
            status=status.HTTP_200_OK
        )
