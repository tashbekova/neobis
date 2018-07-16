from rest_framework import serializers
from CRM.models import Table,User,Category,Role,Meal,MealsToOrder,Order,Department,Status

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

class ServicePercentageSerializers(serializers.ModelSerializer):
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

class MealsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('name', 'price', 'description','category')

class OrderSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    tables = TableSerializer(many=True)
    meals = MealSerializer(many=True)

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
            Meal.objects.create(order=order,**meal)
            
        return order