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
    create_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
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


class MealOffModel(models.Model):
    subscription = models.ForeignKey(PackageModel, on_delete=models.CASCADE)
    date = models.DateField()
    lunch_off = models.BooleanField(default=False)
    dinner_off = models.BooleanField(default=False)
    date_creted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_creted
    
    class Meta:
        verbose_name_plural = "Meals"