from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Task(models.Model):

    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)  

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
