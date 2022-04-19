from django.db import models
User = get_user_model()
# Create your models here.

class DayMeals(models.Model):
   day = models.CharField(max_length=100)

   owner = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)



class FoodComponents(models.Model):
  name = models.CharField(max_length=200)

  carbon_footprint = models.FloatField
