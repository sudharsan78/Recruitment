from django.contrib import admin
from .models import JobPost, Application 

class JobPostAdmin(admin.ModelAdmin):
    list_display = [
            'position', 'country', 'location', 'experience', 
            'primary_skill', 'posted_on',
        ]
    list_filter = ['country', 'location', 'posted_on',]
    
admin.site.register(JobPost, JobPostAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'applied_for', 'email', 'phone_number', 'status']

admin.site.register(Application, ApplicationAdmin)

