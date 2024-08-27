from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages


def user_is_employer(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'employer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_employee(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'candidate':
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Unable to apply for the job. You must register as a candidate to apply.')
            return redirect('jobs:home')

    return wrap