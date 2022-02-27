from rest_framework import serializers

from .models import User, Days, Months

class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = ( 'timestamp', 'consumption', 'temperature' )


class MonthsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = ( 'timestamp', 'consumption', 'temperature' )


class UserSerializer(serializers.ModelSerializer):
    month_max_con = serializers.IntegerField( read_only=True )
    month_min_con = serializers.IntegerField( read_only=True )
    day_max_con = serializers.IntegerField( read_only=True )
    day_min_con = serializers.IntegerField( read_only=True )


    class Meta:
        model = User
        fields = ('name', 'mail', 'month_max_con', 'month_min_con', 'day_max_con', 'day_min_con')