# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_column', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multicolumns',
            name='gutter_width',
            field=models.CharField(default=b'normal', max_length=50, verbose_name='gutter width', choices=[(b'large', 'Large'), (b'normal', 'Normal'), (b'small', 'Small'), (b'none', 'No Gutter')]),
        ),
    ]
