# Generated by Django 4.1.4 on 2023-01-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.IntegerField(max_length=5, unique=True)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Product_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Product_Price', models.FloatField()),
            ],
        ),
    ]
