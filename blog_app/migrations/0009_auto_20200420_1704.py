# Generated by Django 3.0.3 on 2020-04-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20200419_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='country',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='f_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='github_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='linkedin_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='s_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
