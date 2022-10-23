# Generated by Django 4.1.2 on 2022-10-23 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_imagesportproducts_delete_imageproducts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesportproducts',
            options={'verbose_name': 'Картинка спортивного товара', 'verbose_name_plural': 'Картинки спортивных товаров товаров'},
        ),
        migrations.AlterField(
            model_name='imagesportproducts',
            name='sport_products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_sport_product', to='product_app.sport'),
        ),
        migrations.CreateModel(
            name='ImageTVProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_product/%Y', verbose_name='Картинка товара')),
                ('tv_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_tv_product', to='product_app.tv')),
            ],
            options={
                'verbose_name': 'Картинка телевизора',
                'verbose_name_plural': 'Картинки телевизоров',
            },
        ),
        migrations.CreateModel(
            name='ImageToysProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_product/%Y', verbose_name='Картинка товара')),
                ('toys_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_toys_product', to='product_app.toys')),
            ],
            options={
                'verbose_name': 'Картинка игрушки',
                'verbose_name_plural': 'Картинки игрушек',
            },
        ),
        migrations.CreateModel(
            name='ImageGoodsProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_product/%Y', verbose_name='Картинка товара')),
                ('goods_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_goods_product', to='product_app.goods')),
            ],
            options={
                'verbose_name': 'Картинка вещей',
                'verbose_name_plural': 'Картинки вещей',
            },
        ),
    ]
