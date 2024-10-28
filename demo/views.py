from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from . import forms
from . import models


def index(request):
    clients = models.Client.objects.all()
    contacts = models.Contact.objects.all()
    context = {
        "clients": list(clients.values()),
        # "contacts": list(contacts.values()),
    }
    return render(request, "index.html", context)


class ClientCreateView(CreateView):
    model = models.Client
    template_name = "client_create.html"
    success_url = reverse_lazy("home")
    fields = ("name", "contact")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_list"] = models.Contact.objects.all()
        return context


class ContactCreateView(CreateView):
    model = models.Contact
    template_name = "contact_create.html"
    success_url = reverse_lazy("home")
    form_class = forms.ContactForm
    # fields = ("name", "surname", "email")


class ContactDetailView(DetailView):
    model = models.Contact
    template_name = "contact_detail.html"
    context_object_name = "contact"
