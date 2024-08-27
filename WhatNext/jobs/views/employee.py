from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from jobs.decorators import user_is_employee
from accounts.models import *
from accounts.forms import *
from django.views.generic import DetailView, ListView, DeleteView
from jobs.models import *
from django.shortcuts import get_object_or_404


class CandidateProfileView(DetailView):
    model = CandidateProfile
    template_name = 'jobs/employee/profile.html'
    context_object_name = 'profile'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        # Use get_object_or_404 for better error handling
        obj = get_object_or_404(CandidateProfile, user=self.request.user)
        return obj


class CandidateEditProfileView(UpdateView):
    model = CandidateProfile
    form_class = CandidateProfileUpdateForm
    context_object_name = 'employee'
    template_name = 'jobs/employee/edit-profile.html'
    success_url = reverse_lazy('accounts:candidate-profile')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            obj = CandidateProfile.objects.get(user=self.request.user)
        except CandidateProfile.DoesNotExist:
            raise Http404("Profile doesn't exist")
        return obj
    


class CandidateApplicationsView(ListView):
    model = Applicant
    template_name = 'jobs/employee/applications.html'
    context_object_name = 'applications'
    paginate_by = 10

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Applicant.objects.filter(user=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Applicant.status
        return context
    

class CandidateApplicationDeleteView(DeleteView):
    model = Applicant
    template_name = 'jobs/employee/application_confirm_delete.html'
    context_object_name = 'application'
    success_url = reverse_lazy('accounts:candidate-applications')  # Redirect to applications list after delete

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Ensure only the candidate who owns the application can delete it
        return Applicant.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Application deleted successfully!')
        return response