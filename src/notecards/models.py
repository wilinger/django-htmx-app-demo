from django.db import models
from django.urls import reverse_lazy


class Notecard(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(blank=True, max_length=200)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("notecards:detail", kwargs={"pk": self.pk})
