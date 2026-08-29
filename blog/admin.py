from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    search_fields=("title",)
    list_display=("id","title","publish_date","status")
    list_filter=("status",)
    empty_value_display="empty",
    summernote_fields = ('content',)


class Commentadmin(admin.ModelAdmin):
    search_fields=("subject",)
    list_display=("id","subject","post","create_date","approve")
    list_filter=("post","approve")
    empty_value_display="empty"


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,Commentadmin)