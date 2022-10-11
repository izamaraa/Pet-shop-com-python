from django.db import models
import math
class Options(models.TextChoices):
    MALE="Macho"
    FEMALE="Femea"
    DEFAULT= "Não informado"

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age= models.IntegerField()
    weight= models.FloatField()
    sex= models.CharField(max_length=15,choices=Options.choices, default= Options.DEFAULT,)
    group= models.ForeignKey("groups.Group", on_delete= models.CASCADE, related_name="animals", null=True)

    def convert_age_in_human_years(self):
        human_age= 16*math.log(self.age)+31
        return round(human_age,1)

    

