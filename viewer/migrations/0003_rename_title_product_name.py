# Generated by Django 3.2.4 on 2021-06-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
