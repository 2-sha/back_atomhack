from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import DepartmentListSerializer, DepartmentDetailSerializer
from .models import Department


class DepartmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer


class DepartmentDetailView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetailSerializer
