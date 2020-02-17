from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import *
from labApp.forms import RegistrationForm, AuthorizationForm


class MainPage(TemplateView):
    template_name = 'index.html'


class Registration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)


class Autorization(FormView):
    template_name = 'autorization.html'
    form_class = AuthorizationForm
    success_url = '/success/'

    def post(self, request, *args, **kwargs):
        form = AuthorizationForm(data= request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                login(request,user)
                return redirect(self.success_url)
        return render(request, self.template_name, {'form':form})


@login_required(login_url='/error/')
def login_success(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/error/')


def error_auth(request):
    return render(request, 'logout.html')