from rest_framework import serializers
from CRM.models import *
class CategorySerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name','department')

class TableSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Table
        fields = ['name']

class StatusSerializer(serializers.ModelSerializer): 
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Status
        fields = ['name']

class ServicePercentageSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ServicePercentage
        fields = ['percentage']

class RoleSerializer(serializers.ModelSerializer): 
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Role
        fields = ['name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','surname','login','password','email','dateofadd',
                  'phone' )

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('name', 'price', 'description','category')

class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrder
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    tables = TableSerializer(many=True)
    meals = MealsToOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('roles','tables','is_it_open','date','meals')

    def create(self, validated_data):
        roles = validated_data.pop('roles')
        tables = validated_data.pop('tables')
        meals = validated_data.pop('meals')
        
        order=Order.objects.create(**validated_data)

        for role in roles:
            Role.objects.create(order=order, **role)
        for table in tables:
            Table.objects.create(order=order,**table)
        for meal in meals:
            MealsToOrder.objects.create(order=order,**meal)
            
        return order

class CheckSerializer(serializers.ModelSerializer):
    orders =OrderSerializer(many=True)
    percentages = ServicePercentageSerializer(many=True)
    meals = MealsToOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('orders','date','percentages','totalsum','meals')
    
    def create(self, validated_data):
        orders = validated_data.pop('orders')
        percentages = validated_data.pop('percentages')
        meals = validated_data.pop('meals')
        
        check=Check.objects.create(**validated_data)

        for order in orders:
            Order.objects.create(check=check, **role)
        for percentage in percentages:
            ServicePercentage.objects.create(check=check,**table)
        for meal in meals:
            MealsToOrder.objects.create(check=check,**meal)
            
        return check
    