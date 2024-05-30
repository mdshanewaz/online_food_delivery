from django.contrib import admin
from django.utils import timezone
from SubscriptionApp.models import DaysModel, PackageModel, MealOffModel

# Custom admin class for PackageModel
class PackageModelAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date',)

    def save_model(self, request, obj, form, change):
        if not obj.create_date:
            obj.create_date = timezone.now()
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(DaysModel)
admin.site.register(PackageModel, PackageModelAdmin)
admin.site.register(MealOffModel)
