from django.contrib import admin
from django import forms
from .models import Il, Ilce, Customer, SalesRepresentative, Meeting, Product, ProductBrand, Conversation, Visit

@admin.register(Il)
class IlAdmin(admin.ModelAdmin):
    list_display = ['ad']
    search_fields = ['ad']

@admin.register(Ilce)
class IlceAdmin(admin.ModelAdmin):
    list_display = ['ad', 'il']
    search_fields = ['ad']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'company_name', 'customer_type', 'contact_person', 'il', 'ilce']
    search_fields = ['short_name', 'company_name', 'customer_type', 'contact_person']
    list_filter = ['il', 'ilce']

admin.site.register(Customer, CustomerAdmin)

@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'field']
    search_fields = ['user__username', 'full_name', 'field']

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['sales_representative', 'customer', 'date', 'notes']
    search_fields = ['sales_representative__user__username', 'customer__short_name', 'date', 'notes']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']
    search_fields = ['brand_name']

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['meeting', 'product', 'product_brand']
    search_fields = ['meeting__sales_representative__user__username', 'product__name', 'product_brand__brand_name']

class VisitAdminForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.customer:
            self.fields['customer'].initial = instance.customer.il.ad if instance.customer.il else None
            self.fields['customer_ilce'].initial = instance.customer.ilce.ad if instance.customer.ilce else None
        else:
            self.fields['customer'].initial = None
            #self.fields['customer_ilce'].initial = None
        self.fields['customer'].widget.attrs['readonly'] = True
        self.fields['customer'].widget.attrs['readonly'] = True


class VisitAdmin(admin.ModelAdmin):
    form = VisitAdminForm
    list_display = ['customer', 'customer_il', 'customer_ilce', 'product', 'product_brand', 'sales_representative', 'date', 'notes']

admin.site.register(Visit, VisitAdmin)

