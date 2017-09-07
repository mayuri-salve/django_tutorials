# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bucketlist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='owner',
            field=models.ForeignKey(related_name='bucketlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
