from django.contrib import admin
from.models import PatientProfile,DoctorProfile,PatientVitals
# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(PatientVitals)
