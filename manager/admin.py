from django.contrib import admin
# Register your models here.
from .models import Employee,Leave


class AdminEmployee(admin.ModelAdmin):
    list_display=['employee_uid','employee_name']

class AdminLeave(admin.ModelAdmin):
    list_display=['leave_name','leave_alias','leave_color']   

admin.site.register(Employee,AdminEmployee)
admin.site.register(Leave,AdminLeave)