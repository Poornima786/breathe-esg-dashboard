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

    SCOPE_CHOICES = [
        ('SCOPE_1', 'SCOPE_1'),
        ('SCOPE_2', 'SCOPE_2'),
        ('SCOPE_3', 'SCOPE_3'),
    ]

    organization = models.CharField(
        max_length=100,
        default="Demo Enterprise"
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    scope_category = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES,
        default='SCOPE_1'
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

        return f"{self.organization} - {self.source_name}"