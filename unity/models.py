from django.db import models


class Store(models.Model):
    """
    todo: define Store model
    - store name
    - owner
    - url
    - address line 1
    - address line 2
    - city
    - state
    - country
    """
    pass


class Lead(models.Model):
    """
    todo: define Lead model
    - store: Store
    - email address
    - status <option: subscribed, un-subscribed
    - date created
    - date last update
    """
    pass
