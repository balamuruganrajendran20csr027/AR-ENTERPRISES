# Generated by Django 4.1.7 on 2023-04-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('companyname', models.CharField(max_length=20)),
                ('companynumber', models.IntegerField()),
                ('address', models.TextField()),
                ('gst', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
