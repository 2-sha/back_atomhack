from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DepartmentListView, DepartmentDetailView

urlpatterns = [
    path('', DepartmentListView.as_view(), name='departments'),
    path('<int:pk>', DepartmentDetailView.as_view(), name='department'),
]
