from django.shortcuts import render, redirect
from django.contrib import messages

from .models import JobPost
from .forms import ApplicationForm

def careers(request):
    current_openings = JobPost.objects.all()
    context = {
            "current_openings": current_openings, 
            "application_form": ApplicationForm,
        }
    return render(request, 'job_portal/careers.html', context)

def job_post(request, slug_data):
    post = JobPost.objects.get(slug=slug_data)
    context = {"post": post, "application_form": ApplicationForm,}
    return render(request, "job_portal/job_post.html", context)

def apply_opportunity(request):
    if request.method == "POST":
        application_form = ApplicationForm(data=request.POST, files=request.FILES)
        if application_form.is_valid():
            application_form.save()
            messages.add_message(request, messages.INFO, 'Application submited successfully we will review and get back to you soon.')
            return redirect("job_portal:index")
        else:
            return redirect("job_portal:index")
    else:
        return redirect("job_portal:index")

