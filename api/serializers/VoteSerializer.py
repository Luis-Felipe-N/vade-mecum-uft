from rest_framework import serializers
from questions.models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'vote_type', 'autor', 'created_at', 'answer']