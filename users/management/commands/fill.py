from django.core.management import BaseCommand

from school.models import Lesson, Course


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        course_list = [
            {'title': 'backend'},
            {'title': 'frontend'}
        ]

        # prepare_to_fill_base_list = []
        # for course_data in course_list:
        #     prepare_to_fill_base_list.append(Lesson(**course_data))
        # Course.objects.bulk_create(prepare_to_fill_base_list)


        lessons_list = [
            {'course': Course.objects.get(pk=1), 'title': 'Python DevOps', 'description': 'Python development'},
            {'course': Course.objects.get(pk=1), 'title': 'PHP DevOps', 'description': 'PHP development'},
            {'course': Course.objects.get(pk=2), 'title': 'JavaScript DevOps', 'description': 'JavaScript development'},
            {'course': Course.objects.get(pk=2), 'title': 'Designer', 'description': 'Designer Figma'}
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
