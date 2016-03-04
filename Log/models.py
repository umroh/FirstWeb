from django.db import models
from django.utils import timezone


# Create your models here.
class Log_list(models.Model):
    log_name = models.CharField(max_length=200);
    log_content = models.TextField();
