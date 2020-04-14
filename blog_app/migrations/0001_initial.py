# Generated by Django 3.0.3 on 2020-04-14 09:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('s_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('occupation', models.CharField(max_length=50)),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('country', models.CharField(max_length=15)),
                ('gitgub_address', models.CharField(max_length=30)),
                ('linkedin_address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=25)),
                ('profile_pic', models.ImageField(upload_to='author_pic/')),
                ('authorise', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorID', models.IntegerField()),
                ('author_name', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(upload_to='thumbnail_img/')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=5000)),
                ('accessible', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.Author')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('username', models.CharField(max_length=25)),
                ('profile_pic', models.ImageField(upload_to='user_pic')),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=25)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
