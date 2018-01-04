from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import BlogPermissions, MyBlogPermissions
from blogs.serializers import BlogSerializer, MyBlogSerializer


class BlogsViewSet(ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__username']
    order_fields = ['blog_name']


class MyBlogViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = MyBlogSerializer
    permission_classes = [MyBlogPermissions]


    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter(userid=pk)
        return Response()