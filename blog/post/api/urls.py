

from importlib.resources import path

from django.urls import path

from post.api.views import PostDetailAPIView, PostListAPIView

app_name = "post"
urlpatterns =[
    path('list',PostListAPIView.as_view(),name='listpost'),
    path('detail/<slug>',PostDetailAPIView.as_view(),name='detailpost')
]