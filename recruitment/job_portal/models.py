from django.db import models

class JobPost(models.Model):
    position = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    experience = models.CharField(max_length=40)
    primary_skill = models.CharField(max_length=120)
    secondary_skill = models.CharField(max_length=120)
    salary = models.CharField(max_length=60)
    job_description = models.TextField()

    def __str__(self):
        return self.position

