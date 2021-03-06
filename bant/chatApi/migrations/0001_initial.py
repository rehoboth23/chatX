# Generated by Django 3.0.8 on 2020-09-18 16:42

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
            name='ChatUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('isOnline', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(default='profile-pics/default.jpeg', null=True, upload_to='profile-pics', verbose_name='Profile Pic')),
                ('cover_pic', models.ImageField(default='cover/default.jpeg', null=True, upload_to='cover', verbose_name='Cover Pic')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName1', models.CharField(max_length=5000)),
                ('roomName2', models.CharField(max_length=5000)),
                ('roomUsers', models.CharField(max_length=5000)),
                ('chatId', models.IntegerField(default='0')),
                ('mostRecent', models.IntegerField(default='0', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_memo', models.CharField(max_length=2000)),
                ('_date', models.DateTimeField(auto_now_add=True)),
                ('residentRoom', models.CharField(blank=True, max_length=5000)),
                ('residentRoomId', models.CharField(blank=True, max_length=5000)),
                ('_Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to=settings.AUTH_USER_MODEL)),
                ('_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Room', to='chatApi.ChatRoom')),
            ],
        ),
    ]
