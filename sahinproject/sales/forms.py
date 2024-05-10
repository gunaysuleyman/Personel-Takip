from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class VisitForm(forms.ModelForm):
    il = forms.CharField(label='İl', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    ilce = forms.CharField(label='İlçe', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Visit
        fields = ['sales_representative', 'date', 'customer', 'il', 'ilce', 'product', 'product_brand', 'notes']

    def __init__(self, user, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(salesrepresentative__user=user)
        self.fields['sales_representative'].queryset = SalesRepresentative.objects.filter(user=user)

        self.fields['customer'].widget.attrs['id'] = 'id_customer'
        self.fields['il'].widget.attrs['id'] = 'id_il'
        self.fields['ilce'].widget.attrs['id'] = 'id_ilce'

        
    @classmethod
    def for_user(cls, user, *args, **kwargs):
        return cls(user, *args, **kwargs)
    



    