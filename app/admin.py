from django.contrib import admin
from .models import StudentDB
# Register your models here.
@admin.register(StudentDB)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'gender', 'phone', 'address']