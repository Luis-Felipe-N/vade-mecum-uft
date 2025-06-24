from django.contrib import admin
from questions.models import Answer

@admin.register(Answer)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'is_best_answer', 'created_at')
    list_filter = ('is_best_answer', 'created_at')
    search_fields = ('content',)
    raw_id_fields = ('question', 'author')