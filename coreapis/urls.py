from django.urls import path
from .views.follow_view import FollowView
from .views.unfollow_view import UnFollowView
from .views.user_view import UserView
from .views.post_view import PostView
from .views.like_view import LikeView
from .views.unlike_view import UnlikeView
from .views.comment_view import CommentView
from .views.all_posts_view import AllPostsView

urlpatterns = [
    path('follow/<int:user_id>', FollowView.as_view()),
    path('unfollow/<int:user_id>', UnFollowView.as_view()),
    path('user/<int:user_id>', UserView.as_view()),
    path('posts/', PostView.as_view()),
    path('posts/<int:post_id>', PostView.as_view()),
    path('like/<int:post_id>', LikeView.as_view()),
    path('unlike/<int:post_id>', UnlikeView.as_view()),
    path('posts/<int:post_id>', PostView.as_view()),
    path('comment/<int:post_id>', CommentView.as_view()),
    path('all_posts', AllPostsView.as_view())
]
