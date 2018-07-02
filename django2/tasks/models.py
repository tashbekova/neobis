from django.db import models

Types=(
    ('PHONE','PHONE'),
    ('FACEBOOK','FACEBOOK'),
    ('EMAIL','EMAIL')
)
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    imgpath = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "category"

    def str(self):
        return self.name

class Branch(models.Model): 
    latitude = models.CharField(max_length = 200)
    longtitude = models.CharField(max_length = 200)
    addreaa = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "branch"
        
class Contact(models.Model):
    type=models.IntegerField(choices=Types)
    value=models.CharField(max_length=200)

    class Meta:
        verbose_name="contact"

    def str(self):
        return self.type

class Course(models.Model): 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    contacts = models.ManyToManyField('Contact')
    logo = models.URLField()
    branches = models.ManyToManyField('Branch')

    class Meta:
        verbose_name="course"

    def str(self):
        return self.name