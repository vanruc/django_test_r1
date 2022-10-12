from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Store(models.Model):
    store_name = models.CharField(max_length=255)
    store_owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    website_url = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = CountryField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name

    class Meta:
        ordering = ['store_name']


class Leads(models.Model):
    # enumeration for status fields
    class Status(models.TextChoices):
        SUBSCRIPBED = 'SUB', 'Subscribed'
        UNSUBSCRIBED = 'UNS', 'Un-subscribed'

    store = models.ForeignKey(
        to=Store,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    email_address = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default='SUB'
    )

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.email_address
