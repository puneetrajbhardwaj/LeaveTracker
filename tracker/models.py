from django.db import models
from manager.models import Employee,Leave

class Tracker(models.Model):
    tracker_id=models.AutoField(primary_key=True)
    employee= models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    leave=models.ForeignKey(Leave,on_delete=models.DO_NOTHING)
    date=models.DateField()

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['employee','date'],name='composite_primary_key')
        ]
    def __str__(self):
        return str(self.tracker_id)