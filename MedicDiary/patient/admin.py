from django.contrib import admin
from .models import PatientProfile,PatientVitals,Records,LabReports
# from .models import Patient

# admin.site.register(Patient)
admin.site.register(PatientProfile)
admin.site.register(PatientVitals)
admin.site.register(Records)
admin.site.register(LabReports)














# =======================================================================
# =======================================================================

# from .models import patient_details,notes

# Register your models here.
# admin.site.register(patient_details)
# admin.site.register(notes)
