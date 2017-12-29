from django.contrib import admin
from blogs.models import Category, Post

admin.site.site_header = 'WordPlease Backoffice'
admin.site.site_title = 'WordPlease Backoffice'

admin.site.register(Category)
admin.site.register(Post)
