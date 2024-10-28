from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    code = models.CharField(
        max_length=6, unique=True, editable=False, blank=True, null=True
    )
    contact = models.ForeignKey(
        "Contact",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact_detail", args=[self.id])

    class Meta:
        ordering = ["name"]


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    surname = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        ordering = ["surname"]
