from django.urls import path

from api.views import (QuestionAPIView, AnswerAPIView)

urlpatterns = [
    path('question/', QuestionAPIView.as_view(), name='api-question'),
    path('answer/', AnswerAPIView.as_view(), name='api-answer'),
]


