from django.db import models


class MemesModel(models.Model):
    download = models.FileField(upload_to="media/")
