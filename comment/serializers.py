from rest_framework import serializers

from comment.models import Comment
from user_info.serializers import UserDescSerializer


class CommentChildrenSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = ['parent', 'article']


class CommentSerializer(serializers.ModelSerializer):
    # HyperlinkedIdentityField：由当前字段的主键生成
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    # HyperlinkedRelatedField：由关联字段的主键生成，如与评论关联的是文章
    article = serializers.HyperlinkedRelatedField(view_name='article-detail', read_only=True)
    article_id = serializers.IntegerField(write_only=True, allow_null=True, required=True)

    parent = CommentChildrenSerializer(read_only=True)
    parent_id = serializers.IntegerField(write_only=True, allow_null=True, required=True)

    def update(self, instance, validated_data):
        """父级评论只在创建时关联，更新时不用关联"""
        validated_data.pop('parent_id', None)
        return super().update(instance,validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'created': {'read_only': True}
        }
