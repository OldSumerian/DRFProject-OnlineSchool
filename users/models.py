from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE
from school.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Email address", unique=True, help_text="Input email address"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone number",
        **NULLABLE,
        help_text="Input phone number",
    )
    city = models.CharField(
        max_length=50, verbose_name="City", **NULLABLE, help_text="Input city"
    )
    avatar = models.ImageField(
        upload_to="users/", verbose_name="Avatar", **NULLABLE, help_text="Choose avatar"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-date_joined", "-email"]

    def __str__(self):
        return f"User: {self.email}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Lesson")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")
    payment_method = models.CharField(max_length=50, verbose_name="Payment method")
    paid = models.BooleanField(default=False, verbose_name="Paid")
    session_id = models.CharField(
        max_length=255, verbose_name='ID сессии', help_text='input session ID', **NULLABLE)
    link = models.URLField(
        max_length=400, verbose_name='link', help_text='input link for pay',
                           **NULLABLE)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-payment_date"]

    def __str__(self):
        return (
            f"Payment: {self.user.email}, {self.payment_date}, {self.amount}, {self.payment_method}, "
            f"{self.paid}"
        )
