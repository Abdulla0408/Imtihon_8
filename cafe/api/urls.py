from django.urls import path
from .views import StaffViewSet, PositionViewSet, ShiftViewSet, StaffShiftViewSet, StaffAttendanceViewSet

urlpatterns = [
    path('staff/', StaffViewSet.as_view({'get': 'list', 'post': 'create'}), name='staff-list'),
    path('staff/<int:pk>/', StaffViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='staff-detail'),
    path('positions/', PositionViewSet.as_view({'get': 'list', 'post': 'create'}), name='position-list'),
    path('positions/<int:pk>/', PositionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='position-detail'),
    path('shifts/', ShiftViewSet.as_view({'get': 'list', 'post': 'create'}), name='shift-list'),
    path('shifts/<int:pk>/', ShiftViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='shift-detail'),
    path('staffshifts/', StaffShiftViewSet.as_view({'get': 'list', 'post': 'create'}), name='staffshift-list'),
    path('staffshifts/<int:pk>/', StaffShiftViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='staffshift-detail'),
    path('staffattendance/', StaffAttendanceViewSet.as_view({'get': 'list', 'post': 'create'}), name='staffattendance-list'),
    path('staffattendance/<int:pk>/', StaffAttendanceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='staffattendance-detail'),
]
