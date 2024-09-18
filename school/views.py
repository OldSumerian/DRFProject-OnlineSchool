from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from school.models import Course, Lesson
from school.serializer import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes=(~IsModerator,)
        elif self.action == 'destroy':
            self.permission_classes=(IsOwner,)
        elif self.action in ['update', 'partial_update']:
            self.permission_classes=(IsModerator | IsOwner,)
        elif self.action in ['list', 'retrieve']:
            self.permission_classes=(IsOwner, IsModerator,)
        return super().get_permissions()


class LessonCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner, IsModerator,)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner, IsModerator,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner, IsModerator,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner,)
