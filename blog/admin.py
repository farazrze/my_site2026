from django.contrib import admin
from blog.models import Post,Category


class PostAdmin(admin.ModelAdmin):
    search_fields=("title",)
    list_display=("id","title","publish_date","status")
    list_filter=("status",)
    empty_value_display="empty"

admin.site.register(Post,PostAdmin)
admin.site.register(Category)