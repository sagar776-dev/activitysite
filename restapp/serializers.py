from rest_framework import serializers
from .models import User, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('real_name', 'tz')


class MonitorSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id','real_name', 'tz', 'activity_periods')


