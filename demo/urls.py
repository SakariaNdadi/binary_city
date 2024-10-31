from django.urls import path
from . import views, validation

urlpatterns = [
    path("", views.index, name="home"),
    path("client/create/", views.ClientCreateView.as_view(), name="client_create"),
    path("contact/create/", views.ContactCreateView.as_view(), name="contact_create"),
    path(
        "contact/<int:id>/detail/",
        views.ContactDetailView.as_view(),
        name="contact_detail",
    ),
    path("client/<int:pk>/link/", views.ClientLink.as_view(), name="client_link"),
    path(
        "client/<int:client_id>/unlink/<int:contact_id>/",
        views.unlink_client,
        name="client_unlink",
    ),
    path("check_client_name", validation.check_client_name, name="check_client_name"),
]
