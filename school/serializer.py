from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from school.models import Course, Lesson
from school.validators import VideoLinkValidator
from school.models import Subscription


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ("id", "title", "description", "preview", "video_link")
        validators = [VideoLinkValidator(field="video_link")]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
