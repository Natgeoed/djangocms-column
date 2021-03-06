from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

if hasattr(settings, "COLUMN_WIDTH_CHOICES"):
    WIDTH_CHOICES = settings.COLUMN_WIDTH_CHOICES
else:
    WIDTH_CHOICES = (
        ('10%', _("10%")),
        ('25%', _("25%")),
        ('33.33%', _('33%')),
        ('50%', _("50%")),
        ('66.66%', _('66%')),
        ('75%', _("75%")),
        ('100%', _('100%')),
    )

DEFAULT_GUTTER_WIDTH_CHOICES = (
    ('large', _('Large')),
    ('medium', _('Medium')),
    ('small', _('Small')),
    ('collapse', _('No Gutter')),
)
GUTTER_WIDTH_CHOICES = getattr(settings, "GUTTER_WIDTH_CHOICES", DEFAULT_GUTTER_WIDTH_CHOICES)
DEFAULT_GUTTER_WIDTH = getattr(settings, "GUTTER_WIDTH_DEFAULT", GUTTER_WIDTH_CHOICES[1][0])


@python_2_unicode_compatible
class MultiColumns(CMSPlugin):
    """
    A plugin that has sub Column classes
    """
    gutter_width = models.CharField(
        _('gutter width'),
        max_length=50,
        choices=GUTTER_WIDTH_CHOICES,
        default=DEFAULT_GUTTER_WIDTH)
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        plugins = self.child_plugin_instances or []
        return _("%s columns") % len(plugins)


@python_2_unicode_compatible
class Column(CMSPlugin):
    """
    A Column for the MultiColumns Plugin
    """
    width = models.CharField(
        _("width"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[0][0],
        max_length=50
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return "%s" % self.get_width_display()
