from django.contrib import admin
from .models import Posts
from django.utils.html import format_html


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'img')

    def img(self, obj):
        return format_html(
            f'''<a href="{obj.image.url}" target="_blank">
                          <img src="{obj.image.url}" alt="image" width="150" height="100"
                               style="object-fit: cover;"/>
                      </a>'''
        )


