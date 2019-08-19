from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    
    # def summary(self):
    #     return self._summary[0:10]