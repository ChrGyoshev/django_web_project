from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as view
from web_magazine.accounts.decorators import authentication_required
from web_magazine.accounts.forms import CreateUserForm, LoginForm, ChangeForm
from web_magazine.accounts.models import AppUser, Profile



class AddClassToFormFieldMixin:
    def add_class_to_field(self, form, field_name, css_class):
        if field_name in form.fields:
            form.fields[field_name].widget.attrs['class'] = css_class



class SignUp(view.CreateView):
    @method_decorator(authentication_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = 'sign-up.html'
    success_url = reverse_lazy('index')
    form_class = CreateUserForm

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return valid

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password1'].widget.attrs['class'] = 'pass'
        form.fields['password2'].widget.attrs['class'] = 'pass'
        return form


class SignIn(AccessMixin,LoginView):
    template_name = 'login.html'
    next_page = 'index'
    authentication_form = LoginForm

    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('error page'))
        return super().dispatch(request,*args,**kwargs)


    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget.attrs['class'] = 'pass'
        return form

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class SignOut(LogoutView):
    next_page = reverse_lazy('index')


class ProfileDetails(LoginRequiredMixin, view.DetailView):
    template_name = 'profile-details.html'
    model = get_user_model()

    def dispatch(self, request, *args, **kwargs):
        profile = self.request.user
        self.object = self.get_object()
        if profile != self.object:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class EditProfile(view.UpdateView):
    template_name = 'edit-profile.html'
    form_class = ChangeForm
    model = Profile

    def dispatch(self, request, *args, **kwargs):
        profile = self.request.user
        self.object = self.get_object()
        if profile != self.object.user:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse_lazy('profile details', kwargs= {'pk':self.request.user.pk})


    def get_form(self,*args,**kwargs):
        form = super().get_form(*args,**kwargs)
        form.instance.user = self.request.user
        return form


class DeleteProfile(view.DeleteView):
    model = AppUser
    template_name = 'delete-profile.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        profile = self.request.user
        self.object = self.get_object()
        if profile != self.object:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


