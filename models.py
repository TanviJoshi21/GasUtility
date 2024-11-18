from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('inspection', 'Inspection'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    details = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('submitted', 'Submitted'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
        ],
        default='submitted'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.customer.username} - {self.service_type} - {self.status}"


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
