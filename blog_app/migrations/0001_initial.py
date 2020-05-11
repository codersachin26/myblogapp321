# Generated by Django 3.0.3 on 2020-05-10 19:19

from django.conf import settings
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
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('f_name', models.CharField(max_length=20, null=True)),
                ('s_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('profile_pic', models.ImageField(upload_to='user_pic')),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('occupation', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=15, null=True)),
                ('authorise', models.BooleanField(default=False)),
                ('github_address', models.CharField(blank=True, max_length=50, null=True)),
                ('linkedin_address', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram_address', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_author', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=25)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(upload_to='thumbnail_img/')),
                ('upload_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('Programming', 'Programming'), ('Framework', 'Framework'), ('Hacking', 'Hacking'), ('Language', 'Language'), ('Other', 'Other')], default='Other', max_length=30)),
                ('content', models.CharField(max_length=5000)),
                ('accessible', models.BooleanField(blank=True, default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmt_msg', models.CharField(max_length=200)),
                ('u_name', models.CharField(max_length=25)),
                ('cmt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blog')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('tokenID', models.IntegerField()),
                ('is_valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiverID', models.IntegerField()),
                ('msg', models.CharField(max_length=200)),
                ('is_read', models.BooleanField(default=False)),
                ('is_del', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentsReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_msg', models.CharField(max_length=200)),
                ('u_name', models.CharField(max_length=25)),
                ('cmt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blog')),
                ('main_cmt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Comments')),
            ],
        ),
    ]
