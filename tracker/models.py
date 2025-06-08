from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class JobApplication(models.Model):
    class JobStatus(models.TextChoices):
        APPLIED = 'APPLIED', 'Applied'
        INTERVIEW = 'INTERVIEW', 'Interview'
        OFFER = 'OFFER', 'Offer'
        REJECTED = 'REJECTED', 'Rejected'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=JobStatus.choices, default=JobStatus.APPLIED)
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"
