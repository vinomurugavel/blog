from django.contrib import admin
from .models import Post
from .models import Post




# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'created_at')  # Display project name and date
    formfield_overrides = {
        Post._meta.get_field('content'): {'widget': admin.widgets.AdminTextareaWidget}
    }

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview')
    readonly_fields = ('thumbnail_preview')

    def thumbnail_preview(self, obj):
        pass

    thumbnail_preview.short_description = 'Thumbnail Preview'
admin.site.register(Post, PostAdmin)