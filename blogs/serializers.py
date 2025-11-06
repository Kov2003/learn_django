from rest_framework import serializers
from .models import Blog, Comment, Reaction


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    reactions = ReactionSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'