# Generated by Django 4.1.2 on 2022-10-23 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0004_alter_order_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
