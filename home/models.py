from django.db import models
# python manage.py makemigrations:-create changes in file and store in a file
# python manage.oy migrate:-apply thr pending chnages created by makemigrations
# create your models here
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

