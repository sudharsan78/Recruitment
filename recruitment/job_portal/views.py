from django.shortcuts import render

from .models import JobPost

def careers(request):
    current_openings = JobPost.objects.all()
    return render(request, 'job_portal/careers.html', {"current_openings": current_openings,})

def job_post(request, slug_data):
    post = JobPost.objects.get(slug=slug_data)    
    return render(request, "job_portal/job_post.html", {"post": post,})
