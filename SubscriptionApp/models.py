from django.db import models

# Create your models here.

class DaysModel(models.Model):
    numbers = models.IntegerField(max_length=10,)

    def __str__(self):
        return self.numbers
    
    class Meta:
        verbose_name_plural = "Day for Packages"

# class BasiceModel(models.Model):
#     title = models.CharField(max_length=20)
#     numbers = models.ForeignKey(DaysModel, on_delete=models.CASCADE)
#     deposite = models.IntegerField() 
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name_plural = "Categories"