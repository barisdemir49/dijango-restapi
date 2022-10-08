

from rest_framework.generics import  ListAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView
from post.api.serializers import PostInsertUpdateSerializer, Postserializer

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


class PostInsertAPIView(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostInsertUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostInsertUpdateSerializer
    lookup_field='slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer
    lookup_field='slug'
