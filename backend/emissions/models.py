from django.db import models


class EmissionRecord(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('FLAGGED', 'FLAGGED'),
    ]

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    value = models.FloatField()
    unit = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.source