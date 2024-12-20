from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, FormView, RedirectView
from accounts.forms import CandidateRegistrationForm, EmployerRegistrationForm, UserLoginForm
from accounts.models import User


class RegisterEmployeeView(CreateView):
    model = User
    form_class = CandidateRegistrationForm
    template_name = 'accounts/employee/register.html'
    success_url = '/'
    extra_context = {'title': 'Register Employee'}

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        messages.success(self.request, 'Employee registered successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class RegisterEmployerView(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = 'accounts/employer/register.html'
    success_url = '/'
    extra_context = {'title': 'Register Employer'}

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        messages.success(self.request, 'Employer registered successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class LoginView(FormView):
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Login'}

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.GET.get('next', self.success_url)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        messages.success(self.request, 'You are now logged in.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid email or password.')
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    url = '/login'
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super().get(request, *args, **kwargs)