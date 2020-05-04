from datetime import datetime

import pytz
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core import url_names


class Project(models.Model):
    name = models.TextField(_("Name"))
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        db_table = "project"

    def get_absolute_url(self) -> str:
        return reverse(url_names.project, args=(self.pk,))


class Message(models.Model):
    title = models.TextField(_("Title"))
    content = models.TextField(_("Content"), blank=True)
    edited_at = models.DateTimeField(blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "message"

    def get_absolute_url(self) -> str:
        return reverse(url_names.message, args=(self.pk,))

    @property
    def update_url(self) -> str:
        return reverse(url_names.message_update, args=(self.pk,))

    @property
    def delete_url(self) -> str:
        return reverse(url_names.message_delete, args=(self.pk,))

    def clean(self):
        self.edited_at = datetime.now(tz=pytz.utc)
