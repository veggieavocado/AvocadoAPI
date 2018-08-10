from django.db import models

# Create your models here.
class WantedContent(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, default='')
    content = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.company)

class WantedUrl(models.Model):
    urls = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.pk)


class WantedData(models.Model):
    data_name = models.CharField(max_length=20, blank=True, null=True)
    data = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.data)
