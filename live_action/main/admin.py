from django.contrib import admin

# Register your models here.
from .models import Activity


# admin.site.register(Activity)
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['type']




