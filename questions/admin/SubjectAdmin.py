from django.contrib import admin
from questions.models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'icon')
    search_fields = ('name', 'code')