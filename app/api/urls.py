from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api import views


router = DefaultRouter()

router.register('crudapis', views.StudentViewSet , basename='student')

urlpatterns = [
    path('', include(router.urls))
]
