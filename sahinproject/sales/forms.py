from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class VisitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        try:
            print(user)
        except KeyError:
            print("KeyError")
        super(VisitForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['sales_representative'].queryset = SalesRepresentative.objects.filter(user=user)

    class Meta:
        model = Visit
        fields = ['sales_representative', 'date', 'customer', 'product', 'product_brand', 'notes']

    