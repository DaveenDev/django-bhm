# Generated by Django 4.1.7 on 2023-03-31 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_product'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]