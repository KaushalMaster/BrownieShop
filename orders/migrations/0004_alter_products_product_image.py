# Generated by Django 4.1.4 on 2023-01-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Product_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
