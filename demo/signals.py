import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client


def generate_prefix(name):
    words = name.split()
    if len(words) > 1:
        prefix = "".join(word[0].upper() for word in words)[:3]
    else:
        prefix = name[:3].upper()
    while len(prefix) < 3:
        prefix += random.choice(string.ascii_uppercase)
    return prefix


@receiver(post_save, sender=Client)
def generate_client_code(sender, instance, created, **kwargs):
    if created and not instance.code:
        prefix = generate_prefix(instance.name)
        suffix = "".join(random.choices(string.digits, k=3))
        instance.code = f"{prefix}{suffix}"
        while Client.objects.filter(code=instance.code).exists():
            suffix = "".join(random.choices(string.digits, k=3))
            instance.code = f"{prefix}{suffix}"
        instance.save()
