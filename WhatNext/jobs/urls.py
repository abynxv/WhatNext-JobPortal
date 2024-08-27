from django.urls import path, include
from .views import *
from .views.employer import update_application_status  # Add this import

app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('employer/dashboard', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-applicants'),
        path('edit/<int:pk>', JobEditView.as_view(), name='job-edit'),
        path('delete/<int:pk>', JobDeleteView.as_view(), name='job-delete'),
        path('job/<int:job_id>/applicant/<int:applicant_id>/update-status/', 
             update_application_status, 
             name='update_application_status'),
    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
    path('employer/profile/', EmployerProfileView.as_view(), name='employer-profile'),
    path('employer/edit-profile/', EmployerProfileEditView.as_view(), name='employer-edit-profile'),
]