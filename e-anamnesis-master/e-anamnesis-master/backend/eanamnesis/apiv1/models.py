from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sportonuser")
    degree_prefix = models.CharField(max_length=30, blank=True, null=True)
    degree_postfix = models.CharField(max_length=30, blank=True, null=True)
    birth_cert_num = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField()
    post_address = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
