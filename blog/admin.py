from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    search_fields=("title",)
    list_display=("id","title","publish_date","status")
    list_filter=("status",)
    empty_value_display="empty",
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)