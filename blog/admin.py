from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["headline", "content", "pub_date"]
    search_fields = ["headline", "content"]
    list_filter = ["pub_date"]


admin.site.register(Articles, ArticlesAdmin)
