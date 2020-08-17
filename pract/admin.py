from django.contrib import admin

# Register your models here.
from .models import register_patient,register_doctor,Reports
admin.site.register(register_patient)
admin.site.register(register_doctor)
admin.site.register(Reports)