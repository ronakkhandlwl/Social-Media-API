from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authenticate.models import User
from coreapis.models.follow_model import Follow
from rest_framework import permissions


class UnFollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_user_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def is_following(self, follower, following):
        try:
            return Follow.objects.all().filter(follower=follower, following=following)
        except Follow.DoesNotExist:
            return None

    def post(self, request, user_id):
        '''
        Method to unfollow user having user_id = following_id
        '''
        user_instance = self.get_user_id(user_id)
        if not user_instance:
            return Response(
                {"res": "User with given user id does not exist."},
                status=status.HTTP_400_BAD_REQUEST)

        is_following = self.is_following(request.user.id, user_id)
        if not is_following:
            return Response(
                {"res": "You are not following the given user."},
                status=status.HTTP_400_BAD_REQUEST)
        is_following.delete()
        return Response({"res": "Unfollow Successfull"}, status=status.HTTP_200_OK)
