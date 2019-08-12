# Recruitment

Install python 3.7

mkdir project 

cd project 

git clone https://github.com/sudharsan78/Recruitment.git

cd Recruitment

python3.7 -m venv venv

pip install -r requirement.txt

cd recruitment

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

127.0.0.1:8000/admin/

admin can create a job post in "http://127.0.0.1:8000/admin/job_portal/jobpost/add/".

admin can view the application in "http://127.0.0.1:8000/admin/job_portal/application/" 

user can view the current opening in "http://127.0.0.1:8000/careers/" 
and can see the complete job detail by clicking on the post and then click apply button in the post detail page and fill the form and submit to apply for the job



