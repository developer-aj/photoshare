# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoShare', '0002_image_thumbnail2'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'images/'),
            preserve_default=True,
        ),
    ]
