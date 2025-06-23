from rest_framework import serializers
from questions.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'conteudo', 'autor', 'data_criacao', 'pergunta']