from django.db import models

class Example1(models.Model):
    name = models.CharField(max_length=255,null = False),
    curp = models.CharField(max_length = 16, null = False),
    direccion = models.CharField(max_length = 200, null = False),
    edad = models.IntegerField(null  = False),

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Example1'