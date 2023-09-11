from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path(
        "questions-answers/<slug:slug>/",
        qv.AnswerListApiView.as_view(),
        name="answer-list",
    ),

    path(
        "questions-new-answer/<slug:slug>/",
        qv.AnswerCreateApiView.as_view(),
        name="answer-create",
    ),

    path(
        "answers-detail/<uuid:uuid>/",
        qv.AnswerRUDApiView.as_view(),
        name="answer-detail"
    ),

    path(
        "answers-like/<uuid:uuid>/",
        qv.AnswerLikeApiView.as_view(),
        name="answer-like"
    )
]
