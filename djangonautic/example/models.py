from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=120)
    size = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    paradigm = models.CharField(max_length=20, choices=size, null=True)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


