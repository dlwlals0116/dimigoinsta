from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, AccountCreationForm
from articleapp.models import Article
from followapp.models import Follow


has_decorator = [login_required, account_ownership_required]


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        other = self.object
        user = self.request.user

        if user.is_authenticated:
            follow = Follow.objects.filter(user=user, other=other)
        else:
            follow = None

        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, follow=follow, **kwargs)


'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
'''


@method_decorator(has_decorator, 'get')
@method_decorator(has_decorator, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:main')
    template_name = 'accountapp/update.html'


'''
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
'''


'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
'''


@method_decorator(has_decorator, 'get')
@method_decorator(has_decorator, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


'''
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
'''


def success(request):
    return render(request, 'success.html')


@login_required
def main(request):
    return render(request, 'accountapp/main.html')


def logout_view(request):
    logout(request)
    return redirect('/')


'''
def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))
'''

