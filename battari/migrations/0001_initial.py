# Generated by Django 2.1.1 on 2018-10-12 08:04

import battari.util.big_auto_field
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', battari.util.big_auto_field.BigAutoField(primary_key=True, serialize=False)),
                ('following_user_id', models.BigIntegerField()),
                ('follower_user_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', battari.util.big_auto_field.BigAutoField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', battari.util.big_auto_field.BigAutoField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('spotify_id', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', battari.util.big_auto_field.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', battari.util.big_auto_field.BigAutoField(primary_key=True, serialize=False)),
                ('spotify_id', models.CharField(default='', max_length=30)),
                ('displayname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=10)),
                ('icon', models.TextField(default='')),
                ('firebase_token', models.CharField(default='', max_length=160)),
                ('battari_token', models.CharField(default='', max_length=50)),
                ('current_listening_track', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=30, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', battari.util.big_auto_field.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battari.User')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='receive_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battari.User'),
        ),
        migrations.AddField(
            model_name='map',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battari.User'),
        ),
    ]
