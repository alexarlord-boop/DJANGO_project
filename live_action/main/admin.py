from django.contrib import admin

# Register your models here.
from .models import Activity, Goal


# admin.site.register(Activity)
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['type', 'season', 'enviroment_chars', 'extreme']


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['user', 'is_done']

