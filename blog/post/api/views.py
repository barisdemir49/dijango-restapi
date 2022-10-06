

from rest_framework.generics import  ListAPIView,RetrieveAPIView
from post.api.serializers import Postserializer

from post.models import Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class=Postserializer


    def get_queryset(self):
        return super().get_queryset()

class PostDetailAPIView(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer
    lookup_field='slug'
    
