from django.db import models


class ImageURLs(models.Model):
    urls = models.URLField()

    def __str__(self):
        return self.urls


class AdditionalServices(models.Model):
    services = models.CharField(max_length=32)

    def __str__(self):
        return self.services


class Source1(models.Model):
    coordinates = models.CharField(max_length=32)
    number = models.IntegerField()
    address = models.CharField(max_length=256)
    image_urls = models.ManyToManyField(ImageURLs)
    additional_services = models.ManyToManyField(AdditionalServices)


class FuelPrice(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField()
    currency = models.CharField(max_length=32)

    def __str__(self):
        return f' {self.name} {self.price} {self.currency}'


class Source2(models.Model):
    fuel_price = models.ManyToManyField(FuelPrice)


