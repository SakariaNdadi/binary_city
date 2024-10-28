from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("client/create/", views.ClientCreateView.as_view(), name="client_create"),
    path("contact/create/", views.ContactCreateView.as_view(), name="contact_create"),
    path(
        "contact/<int:id>/detail/",
        views.ContactDetailView.as_view(),
        name="contact_detail",
    ),
]
