from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields=("title",)
    list_display=("id","title","publish_date","status")
    list_filter=("status",)
    empty_value_display="empty"

admin.site.register(Post,PostAdmin)