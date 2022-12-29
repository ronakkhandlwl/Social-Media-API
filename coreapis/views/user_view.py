from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authenticate.models import User
from rest_framework import permissions
from coreapis.models.follow_model import Follow


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_user_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id):

        user_instance = self.get_user_id(user_id)
        if not user_instance:
            return Response(
                {"res": "User with given user id does not exist."},
                status=status.HTTP_400_BAD_REQUEST)
        following = Follow.objects.filter(follower=user_id).count()
        followers = Follow.objects.filter(following=user_id).count()
        email = User.objects.get(id=user_id).email
        if not following:
            following = 0
        if not followers:
            followers = 0
        return Response(
            {"Email id": email,
             "Followers": followers,
             "Following": following},
            status=status.HTTP_200_OK)
