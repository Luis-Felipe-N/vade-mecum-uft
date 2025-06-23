from django.contrib import admin
from questions.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'subject', 'status', 'created_at')
    list_filter = ('status', 'subject', 'created_at')
    search_fields = ('title', 'content')
    raw_id_fields = ('author', 'subject') 
