from django.contrib import admin
from questions.models import Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'content_snippet', 'created_at', 'display_total_votes') 
    list_filter = ('created_at', 'updated_at', 'author', 'question')
    search_fields = ('content', 'author__username', 'question__title')
    
    def content_snippet(self, obj):
        return obj.content[:75] + '...' if len(obj.content) > 75 else obj.content
    content_snippet.short_description = "Conteúdo"

    
    def display_total_votes(self, obj):

        return obj.total_votes
    display_total_votes.short_description = "Total de Votos"
    display_total_votes.admin_order_field = 'total_votes'