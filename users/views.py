from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User, Payment
from users.permissions import IsModerator
from users.serializer import UserSerializer, PaymentSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


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

class PaymentCreateView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount = payment.amount
        product = create_stripe_product(payment.course.name)
        price = create_stripe_price(amount, product.id)
        session_id, link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = link
        payment.save()
