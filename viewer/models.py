from django.db import models

# Create your models here.
from django.db.models import Model, CharField, DateField, IntegerField, TextField, ForeignKey, DO_NOTHING, ImageField


class Brand(Model):
    name = CharField(max_length=55)

    def __str__(self):
        return f'{self.name}'

class Fuel(Model):
    name = CharField(max_length=55)

    def __str__(self):
        return f'{self.name}'

class Transmission(Model):
    name = CharField(max_length=55)

    def __str__(self):
        return f'{self.name}'

class Product(Model):
    title = CharField(max_length=128)
    produced = DateField()
    price = IntegerField()
    color = CharField(max_length=55)
    description = TextField()
    transmission = ForeignKey(Transmission, on_delete=DO_NOTHING)
    fuel = ForeignKey(Fuel, on_delete=DO_NOTHING)
    brand = ForeignKey(Brand, on_delete=DO_NOTHING)
    image = ImageField()

    def __str__(self):
        return f'{self.title}'