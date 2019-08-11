import time

from django.db import models
from django.utils.text import slugify

class JobPost(models.Model):
    position = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    experience = models.CharField(max_length=40)
    primary_skill = models.CharField(max_length=120)
    secondary_skill = models.CharField(max_length=120)
    salary = models.CharField(max_length=60)
    job_description = models.TextField()
    posted_on = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.position

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.position + " " + str(time.time())[:6])
            while True:
                print(1)
                if not self.__class__.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break
                slug = slugify(self.position + " " + str(time.time())[:6])
        super().save(*args, **kwargs)

class Application(models.Model):
    APPLICATION_STATUS = (
            ("rejected", "Rejected"), ("accepted", "Accepted"), 
            ("pending", "Pending"),
        )

    applied_for = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    experience = models.CharField(max_length=40)
    skills = models.CharField(max_length=120)
    resume = models.FileField(upload_to="resume/")
    status = models.CharField(max_length=30, choices=APPLICATION_STATUS, default="pending")
