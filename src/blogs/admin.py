from django.contrib import admin
from blogs.models import Category, Post

admin.site.site_header = 'WordPlease Backoffice'
admin.site.site_title = 'WordPlease Backoffice'

admin.site.register(Category)


@admin.register(Post)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'image', 'intro', 'publish_date')
    list_filter = ('categories',)
    search_fields = ('title',)
    readonly_fields = ('created_at', 'modified_at')
    fieldsets = (
        ('General Data', {
            'fields': ('title', 'intro', 'body')
        }),
        ('Categories and Publish Date', {
            'fields': ('categories', 'publish_date')
        }),
        ('Additional Info', {
            'fields': ('user', 'image'),
        }),
        ('Created & Modified', {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',),
            'description': 'These fields are auto-generated'
        }),
    )