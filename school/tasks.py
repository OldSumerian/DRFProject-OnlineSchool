from celery import shared_task
from django.core.mail import send_mail
from config import settings
from school.models import Subscription


@shared_task
def sending_updates(course):

    emails = Subscription.objects.filter(course=course.id).values_list('user__email', flat=True)
    subject = 'Update Course'
    message = f'You can update course: {course.name}'
    if emails:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails
        )
    print('Message sent')