# Generated by Django 4.1.7 on 2023-05-04 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_alter_feedback_address_alter_feedback_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('publicationyear', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='companyname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='contactnumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='gst',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
