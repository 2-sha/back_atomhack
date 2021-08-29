from rest_framework import serializers

from .models import Department
from user.serializers import UserSerializer


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'parent', 'workload')


class DepartmentDetailSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'workload', 'kpi', 'users')
