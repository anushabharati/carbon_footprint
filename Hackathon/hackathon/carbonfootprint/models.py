from django.db import models

# Create your models here.
#class users(models.Model):
 #   user_id = models.IntegerField()

  #  def __str__(self):
   #     return str(self.user_id)

#class device(models.Model):
 #   users_id = models.ForeignKey('device.users', on_delete=models.CASCADE)
  #  device_type = models.CharField(max_length= 100)

class calculation_of_carbon_footprint(models.Model):
   # userss_id = models.ForeignKey('calculation_of_carbon_footprint.users', on_delete=models.CASCADE)
    #device_id = models.ForeignKey('calculation_of_carbon_footprint.device', on_delete=models.CASCADE)
    
    electricty_consumption = models.IntegerField()
    mileage = models.IntegerField()
    family_members = models.IntegerField()
    created_date = models.DateTimeField('created date')


class treek(models.Model):
    progress = models.IntegerField()
    goal = models.IntegerField()
    number_of_trees = models.IntegerField()
    month = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.id)