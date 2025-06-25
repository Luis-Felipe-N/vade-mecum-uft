from rest_framework import serializers
from questions.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'content', 'created_at', 'question']
        read_only_fields = ['author', 'created_at', 'updated_at', 'question']