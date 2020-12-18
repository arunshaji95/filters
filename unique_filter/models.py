from django.db import models

class FilteredValues(models.Model):
    inputs = models.TextField()
    output = models.TextField()

    def __str__(self):
        return '{} ==> {}'.format(self.inputs, self.output)