from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author','counted_views','status','login_required','published_date','created_date')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name' ,'post','approve','created_date')
    list_filter = ('post','approve')
    ordering = ['-created_date']
    search_fields = ['name','post']
    summernote_fields = ('content',)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
