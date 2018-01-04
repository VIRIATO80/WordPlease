from rest_framework import serializers

from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='user.username')
    url = serializers.SerializerMethodField('create_url')

    def create_url(self, blog):
        request = self.context.get('request')
        return request.build_absolute_uri('detail/'+str(blog.user.id))

    class Meta:
        model = Blog
        fields = ['id', 'blog_name', 'blog_description', 'owner', 'url']


class MyBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'intro', 'image', 'publish_date']
