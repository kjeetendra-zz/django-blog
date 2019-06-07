from django.contrib import admin

# Register your models here.

from .models import Subject,Topic,Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('postName', 'created_date', 'topic', 'status')
    list_filter = ('status',)
    search_fields = ('postName', 'content')

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Post, PostAdmin)