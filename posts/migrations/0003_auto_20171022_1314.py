# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.ImageField(default=0, upload_to=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.ImageField(default=0, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=b'', blank=True),
        ),
    ]
