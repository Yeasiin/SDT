from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CarModel



class CreateCarModel(CreateView):
    model = CarModel
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("orders")

    def form_valid(self, form):
        messages.success(self.request,"Model Create Successful")
        return super().form_valid(form)


