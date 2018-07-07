from django.db import models

Types=(
    ('PHONE','PHONE'),
    ('FACEBOOK','FACEBOOK'),
    ('EMAIL','EMAIL')
)
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "category"

    def __str__(self):
        return self.name

class Branch(models.Model): 
    latitude = models.CharField(max_length = 200)
    longtitude = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "branch"
        
class Contact(models.Model):
    type=models.IntegerField(choices=Types)
    value=models.CharField(max_length=200)

    class Meta:
        verbose_name="contact"

    def __str__(self):
        return self.value

class Course(models.Model): 
    category = models.ManyToManyField('Category')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    contacts = models.ManyToManyField('Contact')
    logo = models.URLField()
    branches = models.ManyToManyField('Branch')

    class Meta:
        default_related_name="course"

    def __str__(self):
        return self.name