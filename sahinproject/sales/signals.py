from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth.models import User

@receiver(pre_save, sender=Customer)
def assign_sales_rep(sender, instance, **kwargs):
    if not instance.sales_representative:
        # Müşteri henüz bir satış temsilcisi atanmamışsa
        # Müşteriyi oluşturan kullanıcının satış temsilcisi olarak atanması
        user = instance._meta.model.objects.get(id=instance.created_by_id)
        if hasattr(user, 'salesrepresentative'):
            instance.sales_representative = user.salesrepresentative
