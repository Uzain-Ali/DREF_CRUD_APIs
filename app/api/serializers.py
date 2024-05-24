from rest_framework import serializers
from app.models import StudentDB


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDB
        fields = ['id', 'name', 'email', 'gender', 'phone', 'address']