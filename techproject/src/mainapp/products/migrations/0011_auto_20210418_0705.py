# Generated by Django 2.1.5 on 2021-04-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210418_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees')], max_length=60),
        ),
    ]