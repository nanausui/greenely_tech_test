from rest_framework.generics import GenericAPIView, ListAPIView
import django_filters.rest_framework

from .models import User, Days, Months
from django.db.models import Max, Min

from .serializer import UserSerializer, DaysSerializer, MonthsSerializer


class DataViewSet(ListAPIView):
    queryset = Days.objects.filter(user_id=1)
    serializer_class = DaysSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


    def get_queryset(self):

        resolution = self.request.query_params.get('resolution')
        if resolution == "months":
            queryset = Months.objects.filter(user_id=1)
        else:
            queryset = Days.objects.filter(user_id=1)

        return queryset


    def get_serializer_class(self):
        resolution = self.request.query_params.get('resolution') 
        
        if resolution == "months":
            self.serializer_class = MonthsSerializer
        else:
            self.serializer_class = DaysSerializer

        return self.serializer_class


