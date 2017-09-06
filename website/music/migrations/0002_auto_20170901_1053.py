# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(to='music.Album')),
            ],
        ),
        migrations.RemoveField(
            model_name='songs',
            name='album',
        ),
        migrations.DeleteModel(
            name='Songs',
        ),
    ]
