from django.db import models


class Snippet(models.Model):
    data = models.TextField()