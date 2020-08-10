from django.contrib import admin
from .models import Tasks, Type, Status


class TasksAdmin(admin.ModelAdmin):
    filter_horizontal = ('types',)

admin.site.register(Tasks, TasksAdmin)
admin.site.register(Type)
admin.site.register(Status)