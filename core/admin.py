from django.contrib import admin
from .models import Clinic,Doctor,Queue

# Register your models here.
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Queue)
