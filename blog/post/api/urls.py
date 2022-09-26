

from importlib.resources import path

from django.urls import path

from post.api.views import PostListAPIView

app_name = "post"
urlpatterns =[
    path('list',PostListAPIView.as_view(),name='listpost')
]