from django.db import models

# Create your models here.
class Employ(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eadress=models.CharField(max_length=64)
    def get_sal(self):
        return self.esal