from django.db import models
from LoginApp.models import User
from datetime import datetime, timedelta

# Create your models here.

class DaysModel(models.Model):
    numbers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.numbers)
    
    class Meta:
        verbose_name_plural = "Days Number"


class PackageModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    days = models.ForeignKey(DaysModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    deposite = models.IntegerField( null=True, blank=True) 
    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.create_date:
            self.create_date = datetime.now().date()
        
        self.end_date = self.create_date + timedelta(days=self.days.numbers)

        super(PackageModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Packages"