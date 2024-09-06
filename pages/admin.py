# from os import O_NONBLOCK
from django.contrib import admin
from .models import AboutImage, Team, Contact, Review, Image
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 10px;" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id','first_name',)
    search_fields = ('first_name', 'designation')
    list_filter= ('designation',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','subject', 'message' , 'created_date')
    list_display_links = ('id','name')
    search_fields = ('name',)

class ReviewAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 10px;" />'.format(object.photo.url))
    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'bride_name', 'groom_name', 'city', 'description', 'created_date', 'is_featured' )
    list_display_links = ('id','bride_name', 'groom_name')
    search_fields = ('city', 'bride_name', 'groom_name', 'city')
    list_editable = ('is_featured',)

class ImageAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 10px;" />'.format(object.photo.url))
    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'title', 'created_date', 'is_featured')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_editable = ('is_featured',)

class AboutImageAdmin (admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 10px;" />'.format(object.photo_1.url))
    thumbnail.short_description = 'photo_1'
    list_display = ('id', 'thumbnail')
    list_display_links = ('id', 'thumbnail')

admin.site.register(Team, TeamAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(AboutImage, AboutImageAdmin)


