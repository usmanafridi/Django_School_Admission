
from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('firstapp/<int:student_id>/', views.student_detail, name='student_detail')

]
