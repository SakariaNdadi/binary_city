from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from . import forms
from . import models


def index(request, **kwargs):
    clients = models.Client.objects.all()
    # contacts = models.Contact.objects.all()
    contacts = models.Contact.objects.annotate(client_count=Count("client")).values(
        "id", "name", "surname", "email", "client_count"
    )
    context = {
        "clients": clients,
        "contacts": contacts,
    }
    return render(request, "index.html", context)


class ClientCreateView(CreateView):
    model = models.Client
    template_name = "client_create.html"
    success_url = reverse_lazy("home")
    form_class = forms.ClientForm
    # fields = ("name", "contact")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_list"] = models.Client.objects.all()
        return context


class ClientLink(UpdateView):
    model = models.Contact
    template_name = "link_contact.html"
    fields = ("client",)

    def get_success_url(self):
        return reverse_lazy("client_link", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_list"] = models.Client.objects.all()
        return context


def unlink_client(request, contact_id, client_id):
    contact = get_object_or_404(models.Contact, id=contact_id)
    client = get_object_or_404(models.Client, id=client_id)
    contact.client.remove(client)
    return redirect(reverse("client_link", args=[contact_id]))


class ContactDetailView(DetailView):
    model = models.Contact
    template_name = "contact_detail.html"
    context_object_name = "contact"
