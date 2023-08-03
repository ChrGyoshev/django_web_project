from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class LoginRequiredToAccsses(UserPassesTestMixin):
    def test_func(self):
        return not  self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('error page')

