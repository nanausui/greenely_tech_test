from rest_framework import serializers

from .models import User, Days, Months

class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = ('timestamp', 'consumption', 'temperature')


class MonthsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = ( 'timestamp', 'consumption', 'temperature' )


class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

            max_days_data = Days.objects.filter(user_id = user.id).order_by('consumption').last()
            min_days_data = Days.objects.filter(user_id = user.id).order_by('consumption').first()
            max_months_data = Months.objects.filter(user_id = user.id).order_by('consumption').last()
            min_months_data = Months.objects.filter(user_id = user.id).order_by('consumption').first()

            data["days"] = {
                "timestamp": {
                "minimum": min_days_data.timestamp,
                "maximum": max_days_data.timestamp
                },
                "consumption": {
                "minimum": min_days_data.consumption,
                "maximum": max_days_data.consumption
                },
                "temperature": {
                "minimum": min_days_data.temperature,
                "maximum": max_days_data.temperature
                },
            }

            data["months"] = {
                "timestamp": {
                "minimum": min_months_data.timestamp,
                "maximum": max_months_data.timestamp
                },
                "consumption": {
                "minimum": min_months_data.consumption,
                "maximum": max_months_data.consumption
                },
                "temperature": {
                "minimum": min_months_data.temperature,
                "maximum": max_months_data.temperature
                },
            }

        return data