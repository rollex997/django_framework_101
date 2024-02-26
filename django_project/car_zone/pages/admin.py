from django.contrib import admin
from pages.models import Team

from django.utils.html import format_html
@admin.register(Team)
class TeamsModelAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:40%;"/>'.format(object.photo.url))
    thumbnail.short_description = 'image'
    list_display = ('id','thumbnail','firstname','lastname','designation','photo','facebook_link','twitter_link','created_date')
    list_display_links = ('thumbnail','firstname',)
    search_fields = ('firstname','lastname','designation')
    list_filter=('designation',)