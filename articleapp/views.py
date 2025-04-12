from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin
from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


has_decorator = [login_required, article_ownership_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_decorator, 'get')
@method_decorator(has_decorator, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_decorator, 'get')
@method_decorator(has_decorator, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView, MultipleObjectMixin):
    queryset = Article.objects.order_by('-created_at')
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 25


class ArticleListPopView(ListView, MultipleObjectMixin):
    queryset = Article.objects.order_by('-like_users', 'dislike_users')
    context_object_name = 'article_pop_list'
    template_name = 'articleapp/pop_list.html'
    paginate_by = 25


class ArticleListOldView(ListView, MultipleObjectMixin):
    queryset = Article.objects.order_by('created_at')
    context_object_name = 'article_old_list'
    template_name = 'articleapp/old_list.html'
    paginate_by = 25


def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
        article.dislike_users.remove(request.user)
    return redirect('articleapp:detail', article.pk)


def dislike(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.dislike_users.all():
        article.dislike_users.remove(request.user)
    else:
        article.dislike_users.add(request.user)
        article.like_users.remove(request.user)
    return redirect('articleapp:detail', article.pk)
