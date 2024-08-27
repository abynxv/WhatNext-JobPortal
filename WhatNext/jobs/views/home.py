from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from jobs.forms import ApplyJobForm
from jobs.models import Job, Applicant
from django.shortcuts import redirect
from django.urls import reverse
from jobs.decorators import user_is_employee



class HomeView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context


class SearchView(ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        position = self.request.GET.get('position', '')
        location = self.request.GET.get('location', '')      
        queryset = self.model.objects.all()
        
        if position:
            queryset = queryset.filter(title__icontains=position)
        if location:
            queryset = queryset.filter(location__icontains=location)
        
        return queryset.order_by('-created_at')


class JobListView(ListView):
    model = Job
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'
    def get_queryset(self):
        return Job.objects.select_related('company').all()
    

class JobDetailsView(DetailView):
    model = Job
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        try:
            obj = super().get_object(queryset=queryset)
        except Job.DoesNotExist:
            raise Http404("Job doesn't exist")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # Redirect to a different view or page if job doesn't exist
            return redirect(reverse('jobs:job-list'))  # Replace 'jobs:job-list' with your URL name
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ApplyJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('jobs:home'))

    def get_success_url(self):
        return reverse_lazy('jobs:jobs-detail', kwargs={'id': self.kwargs['job_id']})

    def form_valid(self, form):
        # Check if user already applied for the job
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant.exists():
            messages.info(self.request, 'You have already applied for this job.')
            return HttpResponseRedirect(self.get_success_url())
        
        # Save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)