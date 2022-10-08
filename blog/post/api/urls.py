

from importlib.resources import path

from django.urls import path

from post.api.views import PostDetailAPIView, PostListAPIView,PostInsertAPIView,PostDeleteAPIView,PostUpdateAPIView

app_name = "post"
urlpatterns =[
    path('list',PostListAPIView.as_view(),name='listpost'),
    path('insert',PostInsertAPIView.as_view(),name='insertpost'),
    path('detail/<slug>',PostDetailAPIView.as_view(),name='detailpost'),
    path('update/<slug>',PostUpdateAPIView.as_view(),name='updatepost'),
    path('delete/<slug>',PostDeleteAPIView.as_view(),name='deletepost'),
]