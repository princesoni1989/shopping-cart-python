from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='employees',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
