from django.contrib import admin
from .models import patient_details,notes

# Register your models here.
admin.site.register(patient_details)
admin.site.register(notes)