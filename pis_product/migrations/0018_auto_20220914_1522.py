# Generated by Django 3.0.7 on 2022-09-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_product', '0017_stockout_purchased_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('Kilogram', 'Kilogram'), ('Gram', 'Gram'), ('Litre', 'Litre'), ('Quantity', 'Quantity'), ('Bars', 'Bars')], default='Quantity', max_length=200, null=True),
        ),
    ]
