# Generated by Django 4.1.7 on 2023-05-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_rename_enquiry_enquirie'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirie',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
