#models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Il(models.Model):
    ad = models.CharField(max_length=100, verbose_name=_("İl"))

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("İl")
        verbose_name_plural = _("İller")

class Ilce(models.Model):
    il = models.ForeignKey(Il, on_delete=models.CASCADE, verbose_name=_("İl"))
    ad = models.CharField(max_length=100, verbose_name=_("İlçe"))

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("İlçe")
        verbose_name_plural = _("İlçeler")

class Customer(models.Model):
    short_name = models.CharField(max_length=100, verbose_name=_("Müşteri Kısa Adı"))
    company_name = models.CharField(max_length=100, verbose_name=_("Müşteri Şirket Adı"))
    customer_type = models.CharField(max_length=100, verbose_name=_("Müşteri Tipi"))
    contact_person = models.CharField(max_length=100, verbose_name=_("Görüşülen Kişi"))
    il = models.ForeignKey(Il, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("İl"))
    ilce = models.ForeignKey(Ilce, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("İlçe"))

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _("Müşteri")
        verbose_name_plural = _("Müşteriler")

class SalesRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Kullanıcı"))
    full_name = models.CharField(max_length=100, verbose_name=_("Adı ve Soyadı"))
    field = models.CharField(max_length=100, verbose_name=_("Çalışma Sahası"))
    assigned_customers = models.ManyToManyField(Customer, blank=True, verbose_name=_("Atanmış Müşteriler"))

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username

    class Meta:
        verbose_name = _("Satış Temsilcisi")
        verbose_name_plural = _("Satış Temsilcileri")

class Meeting(models.Model):
    sales_representative = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, verbose_name=_("Satış Temsilcisi"))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_("Müşteri"))
    date = models.DateField(verbose_name=_("Tarih"))
    notes = models.TextField(verbose_name=_("Notlar"))

    class Meta:
        verbose_name = _("Toplantı")
        verbose_name_plural = _("Toplantılar")

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Ürün Adı"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Ürün")
        verbose_name_plural = _("Ürünler")

class ProductBrand(models.Model):
    brand_name = models.CharField(max_length=100, verbose_name=_("Marka Adı"))

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = _("Ürün Markası")
        verbose_name_plural = _("Ürün Markaları")

class Conversation(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name=_("Toplantı"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Ürün"))
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Ürün Markası"))

    class Meta:
        verbose_name = _("Görüşme")
        verbose_name_plural = _("Görüşmeler")

class Visit(models.Model):
    sales_representative = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, verbose_name=_("Satış Temsilcisi"))
    date = models.DateField(verbose_name=_("Tarih"))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_("Müşteri"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Ürün"))
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Ürün Markası"))
    notes = models.TextField(null=True, blank=True, verbose_name=_("Notlar"))
    
    @property
    def customer_il(self):
        return self.customer.il.ad if self.customer.il else None

    @property
    def customer_ilce(self):
        return self.customer.ilce.ad if self.customer.ilce else None
    
    def __str__(self):
        return self.customer.short_name

    class Meta:
        verbose_name = _("Randevu")
        verbose_name_plural = _("Randevular")

