from django.contrib import admin
from .models import tags,Article,MoringaMerch


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

   
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(MoringaMerch)
