import json

from rest_framework import serializers
from .models import Article, Category, Tag
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





class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text',
    )

    def to_internal_value(self, data):
        tags_data = data.get('tags')
        if isinstance(tags_data, list):
            for text in (tags_data):
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

    # category_id 字段的验证器，防止为文章添加不存在的category_id时500错误
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exists.".format(value))
        return value




    class Meta:
        model = Article
        fields = '__all__'





class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情的嵌套序列器，显示每个分类对应文章的article url"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = ['url', 'title']

class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]



