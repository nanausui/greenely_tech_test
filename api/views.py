import django_filters
from rest_framework import viewsets
from django_filters import rest_framework as filters 

from .models import User, Days, Months
from django.db.models import Max, Min

from .serializer import UserSerializer, DaysSerializer, MonthsSerializer

class DataFilter(filters.FilterSet):
    timestamp = filters.DateFromToRangeFilter()

    class Meta:
        model = Days
        fields = ['timestamp'] 


class DataViewSet(viewsets.ModelViewSet):
    queryset = Days.objects.all()
    serializer_class = DaysSerializer
    filter_class = DataFilter 


class LimitViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().filter(
        # filterling with lonin user's id
        id=1
    ).annotate(
        month_max_con=Max('months__consumption'), 
        month_min_con=Min('months__consumption'),
        day_max_con=Max('days__consumption'), 
        day_min_con=Min('days__consumption')
    )
    serializer_class = UserSerializer