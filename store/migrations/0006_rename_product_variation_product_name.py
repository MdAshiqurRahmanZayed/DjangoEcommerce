# Generated by Django 4.1 on 2022-10-29 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='product',
            new_name='product_name',
        ),
    ]