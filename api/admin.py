from django.contrib import admin
from api.models import User, Diagnose, Patient

admin.site.register(User)
admin.site.register(Diagnose)
admin.site.register(Patient)
