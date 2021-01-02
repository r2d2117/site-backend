from rest_framework import serializers
from . import models

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'name',)

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        fields = ('id', 'title', 'content', 'tags', 'image', 'created', 'updated',)
        model = models.Post
