from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from .serializers import UserRegisterSerializer,UserDescSerializer
from .permissions import IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'


    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsSelfOrReadOnly]

        return super().get_permissions()


    # 自定义action
    # detail:
        # True
        # 表示路径格式是xxx / < pk > / action方法名 / == 注意这里pk为username
        # False
        # 表示路径格式是xxx / action方法名 /
    # methods: 声明该action对应的请求方式，列表传递
    @action(detail=True,methods=['get',])
    def info(self, request, username=None):
        queryset = User.objects.get(username=username)
        serializer = UserDescSerializer(queryset,many=False)
        return Response(serializer.data)

    @action(detail=False)
    def sorted(self, request):
        users = User.objects.all().order_by('-username')

        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)