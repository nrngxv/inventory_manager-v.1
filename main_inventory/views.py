from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Inventory_item, Category
from inventory_management.settings import LOW_QUANTITY
from django.contrib import messages
from .forms import User_register_form, Inventory_item
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

class Index(TemplateView):
    template_name = "main_inventory/index.html"


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):

        #filtering data by the id of the item
        items = Inventory_item.objects.filter(user = self.request.user.id).order_by("id")
        low_inventory = Inventory_item.objects.filter(user = self.request.user.id, quantity = LOW_QUANTITY) #global var applied from settings.py

        #checks prime value first, that is n>0
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request, f"{low_inventory.count()} item has low inventory")
            else:
                messages.error(request, f"{low_inventory.count()} item has low inventory")

        low_inventory_ids = Inventory_item.objects.filter(user = self.request.user.id, quantity = LOW_QUANTITY).values_list("id", flat=True)
        return render(request, "main_inventory/dashboard.html", {"item": items, "low_inventory_ids": low_inventory_ids})


class Signup_view(View):
    def get(self, request):
        form = User_register_form()
        return render(request, "main_inventory/signup.html", {"form": form}) #context put "form"
    
    def post(self, request):
        form = User_register_form(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username =  form.cleaned_data["username"],
                password = form.cleaned_data["password1"]
            )

            login(request, user)
            return redirect("index")
        
        return render(request, "main_inventory/signup.html", {"form": form})
    

class Add_item(LoginRequiredMixin, CreateView):
    model = Inventory_item
    form_class = Inventory_item
    template_name = 'main_inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Edit_item(LoginRequiredMixin, UpdateView):
    model = Inventory_item
    form_class = Inventory_item
    template_name = "main_inventory/item_form.html"
    success_url = reverse_lazy("dashboard")


class Delete_item(LoginRequiredMixin, DeleteView):
    model = Inventory_item
    template_name = "main_inventory/delete_item.html"
    success_url = reverse_lazy("dashboard")
    context_object_name = "item"


class Create_view():
    pass