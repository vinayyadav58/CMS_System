# Generated by Django 4.2.2 on 2023-07-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
