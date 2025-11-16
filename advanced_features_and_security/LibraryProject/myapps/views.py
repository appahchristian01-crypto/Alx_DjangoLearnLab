from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Article
from django.urls import reverse_lazy
from .forms import ArticleForm  # assume you have a simple ModelForm for Article


# Function-based view protected for creating an article
@permission_required('myapp.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'myapp/article_form.html', {'form': form})


# Function-based view protected for viewing (optional)
@permission_required('myapp.can_view', raise_exception=True)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'myapp/article_detail.html', {'article': article})


# Class-based view protected for editing
class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'myapp/article_form.html'
    permission_required = 'myapp.can_edit'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})


# Class-based view protected for deleting
class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    permission_required = 'myapp.can_delete'
    raise_exception = True
    success_url = reverse_lazy('article_list')


# List view — require view permission
class ArticleListView(PermissionRequiredMixin, ListView):
    model = Article
    template_name = 'myapp/article_list.html'
    permission_required = 'myapp.can_view'
    raise_exception = True
