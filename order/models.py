from django.db import models


CURRENCY = (
    ('₽', 'Ruble'),
    ('$', 'Dollar'),
    ('€', 'Euro')
)


class Item(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')
    price = models.PositiveIntegerField('Price')
    currency = models.CharField('Currency', max_length=6, choices=CURRENCY, default='$')


class Order(models.Model):
    items = models.ManyToManyField(Item, )


class Discount(models.Model):
    pass


class Tax(models.Model):
    pass
