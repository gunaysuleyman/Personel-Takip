# Generated by Django 4.2.11 on 2024-05-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_visit_notes_visit_product_visit_product_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name': 'Randevu', 'verbose_name_plural': 'Randevular'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='short_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Müşteri Kısa Adı'),
        ),
    ]