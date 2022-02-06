from rest_framework.serializers import ModelSerializer
from feed.models import Post,Media,Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['__all__']
class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ['__all__']
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['__all__']