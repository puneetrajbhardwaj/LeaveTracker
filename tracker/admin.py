from django.contrib import admin
from .models import Tracker
# Register your models here.


class AdminTracker(admin.ModelAdmin):
    list_display=['tracker_id','employee','leave','date']


admin.site.register(Tracker,AdminTracker)