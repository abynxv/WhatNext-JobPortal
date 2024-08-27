from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from jobs.decorators import user_is_employer
from jobs.forms import CreateJobForm
from jobs.models import Job, Applicant
from django.views.generic import UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404, redirect
from accounts.forms import *
from accounts.models import *
from django.http import Http404



class DashboardView(ListView):
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)


class ApplicantPerJobView(ListView):
    model = Applicant
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 10

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        job_id = self.kwargs.get('job_id')
        self.job = get_object_or_404(Job, id=job_id, user=self.request.user)
        return Applicant.objects.filter(job=self.job).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job
        context['status_choices'] = Applicant.status
        return context

    def post(self, request, *args, **kwargs):
        applicant_id = request.POST.get('applicant_id')
        new_status = request.POST.get('status')
        if applicant_id and new_status:
            applicant = get_object_or_404(Applicant, id=applicant_id, job=self.job)
            if new_status in dict(Applicant.STATUS_CHOICES):
                applicant.status = new_status
                applicant.save()
        return redirect(request.path)
    

class JobCreateView(CreateView):
    template_name = 'jobs/create.html'
    form_class = CreateJobForm
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('jobs:employer-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if request.user.is_authenticated and request.user.role != 'employer':
            return reverse_lazy('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class JobEditView(UpdateView):
    model = Job
    form_class = CreateJobForm
    template_name = 'jobs/employer/edit_job.html'
    success_url = reverse_lazy('jobs:employer-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Job.objects.filter(user_id=self.request.user.id)
    
class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/employer/delete_job.html'
    success_url = reverse_lazy('jobs:employer-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Job.objects.filter(user_id=self.request.user.id)

class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'jobs/employer/all-applicants.html'
    context_object_name = 'applicants'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(job__user_id=self.request.user.id)
    

class EmployerProfileView(DetailView):
    model = EmployerProfile
    template_name = 'jobs/employer/profile.html'
    context_object_name = 'profile'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        # Use get_object_or_404 to ensure proper error handling
        obj = get_object_or_404(EmployerProfile, user=self.request.user)
        return obj

class EmployerProfileEditView(UpdateView):
    model = EmployerProfile
    form_class = EmployerProfileUpdateForm
    template_name = 'jobs/employer/edit_profile.html'
    success_url = reverse_lazy('jobs:employer-profile')
    context_object_name = 'profile'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        # Fetch the EmployerProfile based on the logged-in user
        try:
            obj = EmployerProfile.objects.get(user=self.request.user)
        except EmployerProfile.DoesNotExist:
            raise Http404("Profile doesn't exist")
        return obj

    def form_valid(self, form):
        # Optionally handle additional form processing
        return super().form_valid(form)


@login_required
def update_application_status(request, job_id, applicant_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id, user=request.user)
        applicant = get_object_or_404(Applicant, id=applicant_id, job=job)
        new_status = request.POST.get('status')
        if new_status in dict(Applicant.STATUS_CHOICES):
            applicant.status = new_status
            applicant.save()
    return redirect('jobs:employer-applicants', job_id=job_id)
