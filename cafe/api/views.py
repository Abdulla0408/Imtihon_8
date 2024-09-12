from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from lazzat.models import Staff, Position, Shift, StaffShift, StaffAttendance
from .serializers import StaffSerializer, PositionSerializer, ShiftSerializer, StaffShiftSerializer, StaffAttendanceSerializer
from lazzat.permissions import IsStaff, IsOwnerOrStaff

# Staff ViewSet
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()  # Hamma xodimlarni olish
    serializer_class = StaffSerializer  # Ma'lumotlarni serializer orqali qayta ishlash
    permission_classes = [IsAuthenticated, IsStaff]  # Tizimga kirgan staff foydalanuvchilari kirishlari mumkin

# Position ViewSet
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()  # Barcha lavozimlarni olish
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated, IsStaff]  # Faqat staff a'zolari kirishlari mumkin

# Shift ViewSet
class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()  # Barcha smenalarni olish
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated, IsStaff]  # Faqat staff a'zolari kirishlari mumkin

# StaffShift ViewSet
class StaffShiftViewSet(viewsets.ModelViewSet):
    queryset = StaffShift.objects.all()  # Xodimlarning smenalari
    serializer_class = StaffShiftSerializer
    permission_classes = [IsAuthenticated, IsStaff]  # Faqat staff a'zolari kirishlari mumkin

# StaffAttendance ViewSet
class StaffAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StaffAttendance.objects.all()  # Xodimlarning ishtiroki
    serializer_class = StaffAttendanceSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]  # Ishtirokni yaratish uchun faqat authentikatsiyadan o'tgan foydalanuvchilar
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwnerOrStaff]  # Ishtirokni ko'rish uchun faqat egasi yoki staff
        else:
            self.permission_classes = [IsStaff]  # Boshqa harakatlar uchun faqat staff a'zolari
        return super().get_permissions()
