from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    _pub_date = models.DateField(verbose_name='Publication Date')
    body = models.TextField(name='body', max_length=1000)
    image = models.ImageField(name='image', upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50] + '...'

    def pub_date(self):
        return self._pub_date.strftime("%B %-d, %Y")
