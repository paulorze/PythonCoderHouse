# Generated by Django 4.2.6 on 2023-10-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AkaliAlimentosApp', '0005_product_img_product_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]