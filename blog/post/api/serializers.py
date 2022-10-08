from rest_framework import serializers
from post.models import Post


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'slug',
            'uuid',
            'image',
            'createDate',
            'user'

        ]

class PostInsertUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'image'
        ]