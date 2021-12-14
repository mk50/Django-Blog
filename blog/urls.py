from django.urls import path
from .views import StartingPageView, AllPostsView, SinglePostView, ReadLaterView

urlpatterns = [
    path('', StartingPageView.as_view(), name='starting_page'),
    path('posts', AllPostsView.as_view(), name='posts_page'),
    path('posts/<slug:slug>', SinglePostView.as_view(), name='post_detail_page'),
    path('read-later', ReadLaterView.as_view(), name='read_later')
]
