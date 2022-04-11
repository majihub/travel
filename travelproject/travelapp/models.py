from django.db import models

# Create your models here.
class place(models.Model):
    nam=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.nam
class members(models.Model):
    img1=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()
    def __str__(self):
        return self.name
