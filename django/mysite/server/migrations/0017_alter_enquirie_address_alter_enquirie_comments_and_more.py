# Generated by Django 4.1.7 on 2023-05-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_enquirie_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirie',
            name='address',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='comments',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='companyname',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='contactnumber',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='email',
            field=models.CharField(editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='gst',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='enquirie',
            name='name',
            field=models.CharField(editable=False, max_length=20),
        ),
    ]
