from rest_framework import serializers
from .models import Article, Category, Tag, Avatar
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



class AvatarSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')

    class Meta:
        model = Avatar
        fields = '__all__'

class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    """文章列表和详情页的基类"""
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
    avatar = AvatarSerializer(read_only=True)
    avatar_id = serializers.IntegerField(
        write_only=True,
        allow_null=True,
        required=False
    )

    def to_internal_value(self, data):
        tags_data = data.get('tags')
        if isinstance(tags_data, list):
            for text in (tags_data):
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

    default_error_messages = {
        'incorrect_avatar_id': 'Avatar with id {value} not exists.',
        'incorrect_category_id': 'Category with id {value} not exists.',
        'default': 'No more message here..'
    }

    def check_obj_exists_or_fail(self,model,value,message):
        # print(self.default_error_messages)
        if not self.default_error_messages.get(message,None):
            message = 'default'

        if not model.objects.filter(id=value).exists() and value is not None:
            self.fail(message, value=value)

    # category_id 字段的验证器，防止为文章添加不存在的category_id时500错误
    def validate_category_id(self, value):
        self.check_obj_exists_or_fail(
            model=Category,
            value=value,
            message='incorrect_category_id'
        )
        return value

    def validate_avatar_id(self,value):
        self.check_obj_exists_or_fail(
            model=Avatar,
            value=value,
            message='incorrect_avatar_id'
        )
        return value

class ArticleSerializer(ArticleBaseSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'body': {'write_only': True}  # 增加参数，在列表接口处，body可写，但不必显示
        }


class ArticleDetailSerializer(ArticleBaseSerializer):
    # SerializerMethodField()调用get_body_html()，可用于将任何类型的数据添加到对象的序列化表示中
    body_html = serializers.SerializerMethodField
    toc_html = serializers.SerializerMethodField

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

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
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]


