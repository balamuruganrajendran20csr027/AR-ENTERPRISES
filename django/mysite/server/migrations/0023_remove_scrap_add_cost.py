# Generated by Django 4.1.7 on 2023-05-11 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0022_scrap_add_stock_scrap_add_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrap',
            name='Add_cost',
        ),
    ]