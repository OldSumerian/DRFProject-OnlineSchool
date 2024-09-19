from django.urls import path
from school.apps import SchoolConfig
from rest_framework.routers import DefaultRouter
from school.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView, SubscriptionAPIView, SubscriptionListAPIView,
)

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/create/", LessonCreateAPIView.as_view(), name="create lesson"),
    path("lessons/", LessonListAPIView.as_view(), name="list lessons"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="retrieve lesson"),
    path(
        "lessons/update/<int:pk>", LessonUpdateAPIView.as_view(), name="update lesson"
    ),
    path(
        "lessons/delete/<int:pk>", LessonDestroyAPIView.as_view(), name="delete lesson"
    ),
    path('subscription/create/', SubscriptionAPIView.as_view(), name='create subscription'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='list subscription'),
] + router.urls
