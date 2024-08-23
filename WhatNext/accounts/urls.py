from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from jobs.views import CandidateProfileView, CandidateEditProfileView, CandidateApplicationsView, CandidateNotificationsView
from .views import *

app_name = "accounts"

urlpatterns = [
    path('employer/register', RegisterEmployerView.as_view(), name='employer-register'),
    path('candidate/register', RegisterEmployeeView.as_view(), name='candidate-register'),
    path('candidate/profile', CandidateProfileView.as_view(), name='candidate-profile'),
    path('candidate/profile/edit', CandidateEditProfileView.as_view(), name='candidate-profile-edit'),
    path('candidate/applications', CandidateApplicationsView.as_view(), name='candidate-applications'),
    path('candidate/notifications', CandidateNotificationsView.as_view(), name='candidate-notifications'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)