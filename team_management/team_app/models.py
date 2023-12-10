from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    role = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"