from django.db import models
from django.core.validators import MinLengthValidator ,MaxValueValidator
from django.core.validators import MaxValueValidator, MinValueValidator

class Example1(models.Model):
    name = models.CharField(max_length=255,null = False)
    edad = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(1)])
    direccion = models.CharField(max_length = 200)
    curp = models.CharField(max_length = 16,validators=[MinLengthValidator(16)])

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Example1'