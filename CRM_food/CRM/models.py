from django.db import models

# Create your models here.
class Category(models.Model): 
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    
    class Meta:
        default_related_name="Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name

class Meal(models.Model): 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    
    class Meta:
        default_related_name="Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return self.name

class MealsToOrder(models.Model): 
    meal= models.ForeignKey('Meal', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)

    count = models.IntegerField(default=0)
    
    class Meta:
        default_related_name="MealsToOrder"
        verbose_name_plural = "MealsToOrders"


class Role(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name

class User(models.Model): 
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dateofadd = models.DateTimeField(auto_now_add=True)
    phone=models.CharField(max_length=50)
    
    class Meta:
        default_related_name="User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

class Order(models.Model): 
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    is_it_open = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    meals = models.ForeignKey('MealsToOrder', on_delete=models.SET_NULL, null=True)

    date=models.DateTimeField(auto_now_add=True)    
    class Meta:
        default_related_name="Order"
        verbose_name_plural = "Orders"

class Status(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"

    def __str__(self):
        return self.name

class ServicePercentage(models.Model):
    percentage = models.FloatField()
    name='Percentage'
    class Meta:
        verbose_name = 'Percentage'
        verbose_name_plural = 'Percentages'

    def __str__(self):
        return self.name

class Check(models.Model):
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    percentage = models.ForeignKey(ServicePercentage, on_delete=models.SET_NULL, null=True)
    meals = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)

    date=models.DateTimeField(auto_now_add=True)
    totalsum = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Check'
        verbose_name_plural = 'Checks'

    def __str__(self):
        return self.totalsum