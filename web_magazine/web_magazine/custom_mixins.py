from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginRequiredToAccsses(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        return redirect(reverse_lazy('error page'))

    def handle_no_permission(self):
        return redirect('error page')


class ModeratorAdminAccsses(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Moderator').exists() or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        return redirect(reverse_lazy('error page'))
