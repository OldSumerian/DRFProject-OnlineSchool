from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User, Payment
from users.permissions import IsModerator
from users.serializer import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["payment_date"]
    filterset_fields = (
        "course",
        "lesson",
        "payment_method",
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
