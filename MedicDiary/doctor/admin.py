from django.contrib import admin
from .models import doc_details
from .models import patient_doc_config,records
# Register your models here.
admin.site.register(doc_details)
admin.site.register(patient_doc_config)
admin.site.register(records)