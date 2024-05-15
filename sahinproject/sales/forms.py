from django import forms
from .models import *
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class VisitForm(forms.ModelForm):
    il = forms.CharField(label='İl', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    ilce = forms.CharField(label='İlçe', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    date = forms.DateField(label='Tarih', widget=forms.DateInput(format='%d.%m.%y', attrs={'type': 'text', 'placeholder': 'GG.AA.YYYY'}))
    view_all_customers = forms.BooleanField(label='Tüm Müşteriler', required=False)
    class Meta:
        model = Visit
        fields = ['sales_representative', 'date', 'customer', 'view_all_customers', 'il', 'ilce', 'product', 'product_brand', 'notes']

    def __init__(self, user, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)

        # Sales representative alanını giriş yapan kullanıcı ile doldur
        #print("DEBUG: User:", user)
        sales_rep = SalesRepresentative.objects.get(user=user)
        #print("DEBUG: Sales Representative:", sales_rep)
        self.fields['sales_representative'].initial = sales_rep
        self.fields['sales_representative'].widget = forms.HiddenInput()
            
        self.fields['customer'].queryset = Customer.objects.filter(salesrepresentative__user=user)
        self.fields['sales_representative'].queryset = SalesRepresentative.objects.filter(user=user)

        self.fields['sales_representative'].widget.attrs['id'] = 'id_sales_representative'
        self.fields['customer'].widget.attrs['id'] = 'id_customer'
        self.fields['il'].widget.attrs['id'] = 'id_il'
        self.fields['ilce'].widget.attrs['id'] = 'id_ilce'
           
    @classmethod
    def for_user(cls, user, *args, **kwargs):
        return cls(user, *args, **kwargs)
    



    