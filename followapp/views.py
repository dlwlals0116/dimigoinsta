from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView
from articleapp.models import Article
from followapp.models import Follow


@method_decorator(login_required, 'get')
class FollowView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('accountapp:detail', kwargs={'pk': self.request.GET.get('account_pk')})

    def get(self, request, *args, **kwargs):
        other = get_object_or_404(User, pk=self.request.GET.get('account_pk'))
        user = self.request.user
        follow = Follow.objects.filter(user=user, other=other)

        if follow.exists():
            follow.delete()
        else:
            Follow(user=user, other=other).save()

        return super(FollowView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class FollowListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'followapp/list.html'
    paginate_by = 25

    def get_queryset(self):
        others = Follow.objects.filter(user=self.request.user).values_list('other')
        article_list = Article.objects.filter(writer__in=others)
        return article_list

