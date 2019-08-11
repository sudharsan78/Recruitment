from django.shortcuts import render

def careers(request):
    return render(request, 'job_portal/careers.html')
