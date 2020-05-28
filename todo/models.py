from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # characters/text in it to prevent unnamed items
    done = models.BooleanField(null=False, blank=False, default=False)
    # add the defaulted value

    def __str__(self):
        return self.name
        # returns the name of the inputted thing
