from django.db import models
from django.utils.translation import gettext_lazy as _

class Portfolio(models.Model):

    field_block = models.CharField(
        max_length=100,
        verbose_name=_('Field Block Name'),
        help_text=_('Name of the field block')
    )

    text_data = models.TextField(
        verbose_name=_('Text Data'),
        help_text=_('Text Data for the field with HTML paragraph config'),
        blank=True,
        null=True
    )

    file_path = models.FileField(
        blank=True,
        null=True,
        verbose_name=_('Path to HTML')
    )

    url_link = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Link to project'),
        help_text=_('URL clickable link to AI/ML projects')
    )

    date_uploaded = models.DateField(
        auto_now_add=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.field_block} [{self.file_path}]'