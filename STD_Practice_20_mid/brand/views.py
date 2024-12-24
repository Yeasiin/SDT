from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CarBrand



class CreateBrand(CreateView):
    model = CarBrand
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("orders")
    
    def form_valid(self, form):
        messages.success(self.request,"Brand Created")
        return super().form_valid(form)
    
