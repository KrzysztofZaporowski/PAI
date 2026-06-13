from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from .models import DatabaseSample

class DatabaseListView(ListView):
    model = DatabaseSample
    template_name = 'repository/list.html'
    context_object_name = 'databases'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        sort = self.request.GET.get('sort', 'name')
        
        if query:
            queryset = queryset.filter(name__icontains=query)
        
        if sort in ['name', '-name']:
            queryset = queryset.order_by(sort)
            
        return queryset

class DatabaseDetailView(DetailView):
    model = DatabaseSample
    template_name = 'repository/detail.html'
    context_object_name = 'db'

class DatabaseCreateView(LoginRequiredMixin, CreateView):
    model = DatabaseSample
    fields = ['name', 'author', 'topic', 'size_class', 'download_link', 'description']
    template_name = 'repository/form.html'
    success_url = reverse_lazy('repository:list')

class DatabaseUpdateView(LoginRequiredMixin, UpdateView):
    model = DatabaseSample
    fields = ['name', 'author', 'topic', 'size_class', 'download_link', 'description']
    template_name = 'repository/form.html'
    success_url = reverse_lazy('repository:list')

    def get_queryset(self):
        # Implementacja ochrony przed współbieżnością (blokada wiersza podczas edycji)
        return super().get_queryset().select_for_update()

    @transaction.atomic
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DatabaseDeleteView(LoginRequiredMixin, DeleteView):
    model = DatabaseSample
    template_name = 'repository/confirm_delete.html'
    success_url = reverse_lazy('repository:list')
