from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.serializer import AccountSerializer
from users.models import Account


class AccountListCreateAPIView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return self.request.user

class AccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return self.request.user

