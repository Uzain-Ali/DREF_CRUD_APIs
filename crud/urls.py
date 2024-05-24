
from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('insert', views.insertData, name="insertData"),
    path('update/<id>', views.updateData, name="updateData"),
    path('delete/<id>', views.deleteData, name="deleteData"),
    path('api/', include('app.api.urls'))
]
