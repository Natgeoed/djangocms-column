# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from djangocms_column.models import GUTTER_WIDTH_CHOICES, DEFAULT_GUTTER_WIDTH


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_column', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multicolumns',
            name='gutter_width',
            field=models.CharField(default=DEFAULT_GUTTER_WIDTH, max_length=50, verbose_name='gutter width', choices=GUTTER_WIDTH_CHOICES),
        ),
    ]
