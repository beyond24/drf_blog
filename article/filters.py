# 定制过滤器类
import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    body = django_filters.CharFilter(field_name='body',lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ('title','body')