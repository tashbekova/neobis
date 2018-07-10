from django.db import models

CONTACT_TYPES=(
    (1,'PHONE'),
    (2,'FACEBOOK'),
    (3,'EMAIL')
)
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Branch(models.Model): 
    latitude = models.CharField(max_length = 200)
    longtitude = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='branches', default = '')

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        
class Contact(models.Model):
    type=models.IntegerField(choices=CONTACT_TYPES)
    value=models.CharField(max_length=200)

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='contacts', default = '')

    class Meta:
        verbose_name="contact"

    def __str__(self):
        return self.value

class Course(models.Model): 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    logo = models.URLField()

    class Meta:
        default_related_name="course"

    def __str__(self):
        return self.name