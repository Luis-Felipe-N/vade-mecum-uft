from django.urls import path

from api.views import (QuestionAPIView, AnswerAPIView, VoteAnswerAPIView)

app_name = 'api'

urlpatterns = [
    path('question/', QuestionAPIView.as_view(), name='api-question'),
    path('answer/', AnswerAPIView.as_view(), name='api-answer'),
    path('answers/<int:answer_id>/vote/<str:vote_type>/', VoteAnswerAPIView.as_view(), name='api-vote-answer'),
]


