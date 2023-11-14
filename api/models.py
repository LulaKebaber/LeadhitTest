from djongo import models


class FormTemplate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    fields = models.JSONField()
