from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .permisssions import IsAdminUserOrReadOnly

from article.models import Article, Category, Tag, Avatar
# from article.serializers import ArticleListSerializer, ArticleDetailSerializer
from article.serializers import ArticleSerializer, CategorySerializer, CategoryDetailSerializer, TagSerializer, \
    ArticleDetailSerializer, AvatarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ArticleFilter


# Create your views here.

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleListSerializer(data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#
#     def get_obj(self, pk):
#         return get_object_or_404(Article, id=pk)
#
#     def get(self, request, pk):
#         article = self.get_obj(pk)
#         serializer = ArticleDetailSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         article = self.get_obj(pk)
#         serializer = ArticleDetailSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         article = self.get_obj(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         """
#         perform_create() ????????? ListCreateAPIView ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
#         :param serializer:
#         :return:
#         """
#         serializer.save(author=self.request.user)
#
#
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]

# ???????????????
class ArticleViewSet(viewsets.ModelViewSet):

    # ??????rest?????????search
    filter_backends = [SearchFilter]
    search_fields = ['title','body']

    # ??????django-filter??????????????????,??????????????????
    # filterset_class = ArticleFilter

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    # perform_create() ????????? ListCreateAPIView ????????????????????????????????????????????????????????????
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # ?????? get_queryset() ?????????????????????;???????????????django-filter
    # def get_queryset(self):
    #     queryset = self.queryset
    #     username = self.request.query_params.get('username', None)
    #
    #     if username:
    #         queryset = queryset.filter(author__username=username)
    #     return queryset
    def get_serializer_class(self):
        """???????????????????????????????????????????????????"""
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

    # ???????????????????????????
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None



class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]