from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from .models import DatabaseSample, Question, Answer

class DatabaseListView(ListView):
    model = DatabaseSample
    template_name = 'repository/list.html'
    context_object_name = 'databases'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        author = self.request.GET.get('author')
        size_class = self.request.GET.get('size_class')
        sort = self.request.GET.get('sort', 'name')
        
        if query:
            if self.request.user.is_authenticated:
                from django.db.models import Q
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query) |
                    Q(questions__content__icontains=query) |
                    Q(questions__answers__content__icontains=query)
                ).distinct()
            else:
                queryset = queryset.filter(name__icontains=query)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if size_class:
            queryset = queryset.filter(size_class=size_class)
        
        if sort in ['name', '-name']:
            queryset = queryset.order_by(sort)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size_choices'] = DatabaseSample.SIZE_CHOICES
        return context

class DatabaseDetailView(DetailView):
    model = DatabaseSample
    template_name = 'repository/detail.html'
    context_object_name = 'db'

class DatabaseCreateView(LoginRequiredMixin, CreateView):
    model = DatabaseSample
    fields = ['name', 'author', 'topic', 'size_class', 'download_link', 'description', 'complexity', 'schema_image', 'ddl_file']
    template_name = 'repository/form.html'
    success_url = reverse_lazy('repository:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class DatabaseUpdateView(LoginRequiredMixin, UpdateView):
    model = DatabaseSample
    fields = ['name', 'author', 'topic', 'size_class', 'download_link', 'description', 'complexity', 'schema_image', 'ddl_file']
    template_name = 'repository/form.html'
    success_url = reverse_lazy('repository:list')

    def get_queryset(self):
        # Implementacja ochrony przed współbieżnością (blokada wiersza podczas edycji)
        return super().get_queryset().filter(owner=self.request.user).select_for_update()

    @transaction.atomic
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DatabaseDeleteView(LoginRequiredMixin, DeleteView):
    model = DatabaseSample
    template_name = 'repository/confirm_delete.html'
    success_url = reverse_lazy('repository:list')

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'bazę danych'
        context['object_description'] = self.object.name
        context['cancel_url'] = reverse_lazy('repository:detail', kwargs={'pk': self.object.pk})
        return context

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['content']
    template_name = 'repository/form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.database = get_object_or_404(DatabaseSample, pk=self.kwargs['pk'])
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('repository:detail', kwargs={'pk': self.kwargs['pk']})

class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['content']
    template_name = 'repository/form.html'
    
    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        if question.database.owner != self.request.user:
            return self.handle_no_permission() # Only database owner can answer
        form.instance.author = self.request.user
        form.instance.question = question
        return super().form_valid(form)
        
    def get_success_url(self):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return reverse_lazy('repository:detail', kwargs={'pk': question.database.pk})

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'repository/confirm_delete.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
        
    def get_success_url(self):
        return reverse_lazy('repository:detail', kwargs={'pk': self.object.database.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'pytanie'
        context['object_description'] = self.object.content[:100]
        context['cancel_url'] = reverse_lazy('repository:detail', kwargs={'pk': self.object.database.pk})
        return context

class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    model = Answer
    template_name = 'repository/confirm_delete.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
        
    def get_success_url(self):
        return reverse_lazy('repository:detail', kwargs={'pk': self.object.question.database.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'odpowiedź'
        context['object_description'] = self.object.content[:100]
        context['cancel_url'] = reverse_lazy('repository:detail', kwargs={'pk': self.object.question.database.pk})
        return context
