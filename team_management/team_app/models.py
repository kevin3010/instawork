from django.db import models

class TeamMember(models.Model):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('regular', 'regular'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"