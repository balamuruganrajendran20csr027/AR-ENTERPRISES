# Generated by Django 4.1.7 on 2023-05-06 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0020_alter_scrap_current_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='current_cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='current_stock',
            field=models.IntegerField(),
        ),
    ]
