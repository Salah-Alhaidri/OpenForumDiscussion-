

from django.contrib import admin
from .models import ForumSectionModel, forummodel
from django.utils.safestring import mark_safe
  
@admin.register(forummodel)
class ForumModelAdmin(admin.ModelAdmin):
    list_display = ('ForumTitile', 'ForumDescription', 'ForumImage')
    search_fields = ('ForumTitile',)
    list_filter = ('ForumTitile',)
    list_editable=('ForumDescription',)
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.ForumImage.url}" style="width: 40px; height: 40px; object-fit: cover;"/>')
        return 'No Image'
    image_preview.short_description = 'Image Preview'  # Title for the column
        
    # def ForumImage_preview(self, obj):
    #     if obj.ForumImage:
    #         return mark_safe(f'<img src="{obj.ForumImage.url}" style="width: 40px; height: 40px; object-fit: cover;"/>')
    #     return "No Image"
    # ForumImage_preview.short_description = "Image Preview"

@admin.register(ForumSectionModel)
class ForumSectionModelAdmin(admin.ModelAdmin):
    list_display = ('SectionSubject', 'board', 'created_by', 'views', 'created_dt', 'updated_by', 'updated_dt')
    search_fields = ('SectionSubject', 'board__ForumTitile', 'created_by__username')
    list_filter = ('board', 'created_dt', 'updated_dt')
    autocomplete_fields = ('board', 'created_by', 'updated_by')
    ordering = ('-created_dt',)
    fieldsets = (
        (None, {
            'fields': ('SectionSubject', 'board', 'views'),
        }),
        ('Created Info', {
            'fields': ('created_by', 'created_dt'),
            'classes': ('collapse',)
        }),
        ('Updated Info', {
            'fields': ('updated_by', 'updated_dt'),
            'classes': ('collapse',)
        }),
    )
