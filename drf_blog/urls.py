"""drf_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from article import views

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # drf登录视图
    path('api-auth/', include('rest_framework.urls')),

    # 文章 改用视图集生成
    # path('api/article/', include('article.urls', namespace='article')),

    # 使用viewset自动生成路由
    path('api/', include(router.urls))
]
