# Generated by Django 4.1.2 on 2022-10-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0002_alter_order_customer'),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='order_app.order', verbose_name='Заказы покупателя'),
        ),
    ]