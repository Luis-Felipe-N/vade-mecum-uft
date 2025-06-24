from django.contrib import admin
from questions.models import Vote

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('answer', 'author', 'created_at')
    list_filter = ( 'created_at',)
    search_fields = ('answer',)
    raw_id_fields = ('answer', 'author')