from django.forms import ModelForm
from SubscriptionApp.models import PackageModel

# Forms Stat here
class PackageForm(ModelForm):
    class Meta:
        model = PackageModel
        fields = ('days','deposite')

        