# Generated by Django 4.1.7 on 2023-05-04 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_delete_scarp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Enquiry',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]