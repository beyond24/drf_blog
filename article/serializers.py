from rest_framework import serializers
from .models import Article
from user_info.serializers import UserDescSerializer


# class ArticleListSerializer(serializers.ModelSerializer):
#     author = UserDescSerializer(read_only=True)
#     url = serializers.HyperlinkedIdentityField(view_name='article:detail')
#     class Meta:
#         model = Article
#         fields = [
#             'id',
#             'url',
#             'title',
#             'created',
#             'author',
#         ]
#         # read_only_fields = ['author']
#
#
# class ArticleDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Article
#         fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model =Article
        fields = '__all__'
