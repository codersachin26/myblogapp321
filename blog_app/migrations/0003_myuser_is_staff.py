# Generated by Django 3.0.3 on 2020-04-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200414_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]