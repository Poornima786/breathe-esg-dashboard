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

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    source_name = models.CharField(
        max_length=100
    )

    value = models.FloatField()

    unit = models.CharField(
        max_length=50
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    original_file = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):

        return f"{self.source_type} - {self.source_name}"