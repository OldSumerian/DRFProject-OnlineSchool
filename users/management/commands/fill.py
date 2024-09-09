from django.core.management import BaseCommand

from school.models import Lesson


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        lessons_list = [
            {'course': 'backend', 'title': 'Python DevOps', 'description': 'Python development'},
            {'course': 'backend', 'title': 'PHP DevOps', 'description': 'PHP development'},
            {'course': 'frontend', 'title': 'JavaScript DevOps', 'description': 'JavaScript development'},
            {'course': 'frontend', 'title': 'Designer', 'description': 'Designer Figma'}
        ]

        # lesson = Lesson.objects.create(
        #     course_id=1,
        #     title='Introduction to Programming',
        #     description='This lesson introduces you to the basics of programming.',
        #     preview='path/to/preview.jpg',
        #     video_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        # )

        prepare_to_fill_base_list = []
        for lesson_data in lessons_list:
            prepare_to_fill_base_list.append(Lesson(**lesson_data))
        Lesson.objects.bulk_create(prepare_to_fill_base_list)
