from django.contrib import admin
from .models import Customer, SalesRepresentative, Il, Ilce, Meeting, Product, ProductBrand, Conversation

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'company_name', 'customer_type', 'contact_person')

class CustomerInline(admin.TabularInline):
    model = SalesRepresentative.assigned_customers.through
    extra = 1

@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    inlines = (CustomerInline,)
    list_display = ('user', 'full_name', 'field')

class IlceInline(admin.TabularInline):
    model = Ilce
    extra = 1

@admin.register(Il)
class IlAdmin(admin.ModelAdmin):
    inlines = (IlceInline,)
    list_display = ('ad', 'id')

@admin.register(Ilce)
class IlceAdmin(admin.ModelAdmin):
    list_display = ('il', 'ad')

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('sales_representative', 'customer', 'date')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('product', 'brand_name')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'product', 'product_brand')
