# Generated by Django 4.1.7 on 2023-05-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_rename_companynumber_feedback_contactnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='address',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comments',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='companyname',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='contactnumber',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='gst',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(editable=False, max_length=20),
        ),
    ]