# Generated by Django 4.2.11 on 2024-04-30 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100, verbose_name='Müşteri Kısa Adı')),
                ('company_name', models.CharField(max_length=100, verbose_name='Müşteri Şirket Adı')),
                ('customer_type', models.CharField(max_length=100, verbose_name='Müşteri Tipi')),
                ('contact_person', models.CharField(max_length=100, verbose_name='Görüşülen Kişi')),
            ],
            options={
                'verbose_name': 'Müşteri',
                'verbose_name_plural': 'Müşteriler',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ürün Adı')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
        migrations.CreateModel(
            name='SalesRepresentative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Adı ve Soyadı')),
                ('field', models.CharField(max_length=100, verbose_name='Çalışma Sahası')),
                ('assigned_customers', models.ManyToManyField(blank=True, to='sales.customer', verbose_name='Atanmış Müşteriler')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Satış Temsilcisi',
                'verbose_name_plural': 'Satış Temsilcileri',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, verbose_name='Marka Adı')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product', verbose_name='Ürün')),
            ],
            options={
                'verbose_name': 'Ürün Markası',
                'verbose_name_plural': 'Ürün Markaları',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Tarih')),
                ('notes', models.TextField(verbose_name='Notlar')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.customer', verbose_name='Müşteri')),
                ('sales_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.salesrepresentative', verbose_name='Satış Temsilcisi')),
            ],
            options={
                'verbose_name': 'Toplantı',
                'verbose_name_plural': 'Toplantılar',
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.meeting', verbose_name='Toplantı')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product', verbose_name='Ürün')),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.productbrand', verbose_name='Ürün Markası')),
            ],
            options={
                'verbose_name': 'Görüşme',
                'verbose_name_plural': 'Görüşmeler',
            },
        ),
    ]