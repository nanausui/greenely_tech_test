from rest_framework.generics import ListAPIView
import django_filters.rest_framework

from .models import User, Days, Months
from django.db.models import Max, Min

from .serializer import DaysSerializer, MonthsSerializer, LimitSerializer


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


class LimitViewSet(ListAPIView):
    queryset = User.objects.filter(id=1)
    serializer_class = LimitSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        print(obj)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

