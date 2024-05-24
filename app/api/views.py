from app.models import StudentDB
from app.api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentDB.objects.all()
    serializer_class = StudentSerializer
    authentication_classes= [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
