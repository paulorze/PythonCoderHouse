# Generated by Django 4.2.6 on 2023-11-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AkaliAlimentosApp', '0020_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='ordertoproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='ordertoproduct',
            name='product_name',
            field=models.CharField(default='asd', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordertoproduct',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordertoproduct',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=1233, max_digits=8),
            preserve_default=False,
        ),
    ]
