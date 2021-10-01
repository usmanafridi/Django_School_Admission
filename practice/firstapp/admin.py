from django.contrib import admin

# Register your models here.

from .models import Admission


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
	list_display= ['name', 'father_name', 'city','score','sex','age']
