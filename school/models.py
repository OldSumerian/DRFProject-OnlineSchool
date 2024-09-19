from django.db import models

from config import settings
from config.settings import NULLABLE


class Course(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Course Title", help_text="input course title"
    )
    description = models.TextField(
        verbose_name="Course Description",
        help_text="input course description",
        **NULLABLE,
    )
    preview = models.ImageField(
        verbose_name="Course Preview", help_text="insert course preview", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Course Owner",
        help_text="user who owns the course",
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"Course: {self.title}"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, verbose_name="Course", on_delete=models.CASCADE, related_name="lessons"
    )
    title = models.CharField(
        max_length=50,
        **NULLABLE,
        verbose_name="Lesson Title",
        help_text="Input lesson Title",
    )
    description = models.TextField(
        **NULLABLE,
        verbose_name="Lesson Description",
        help_text="Input lesson description",
    )
    preview = models.ImageField(
        **NULLABLE, verbose_name="Lesson Preview", help_text="Insert lesson preview"
    )
    video_link = models.URLField(
        **NULLABLE, verbose_name="Video Link", help_text="Insert video link"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Lesson Owner",
        on_delete=models.SET_NULL,
        help_text="user who owns the lesson",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"Lesson: {self.title}, Course: {self.course}"


class Subscription(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="subscription_user",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Course_subscription",
        related_name="subscription_course",
    )

    def __str__(self):
        return f"{self.user} - subscription: {self.course}"

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
