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

class RoleSerializer(serializers.ModelSerializer): 
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Role
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('type', 'value')

class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ('name', 'logo', 'description', 'category', 'contacts', 'branches')

    def create(self, validated_data):
        contacts=validated_data.pop('contacts')
        branches=validated_data.pop('branches')

        course=Course.objects.create(**validated_data)

        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        for branch in branches:
            Branch.objects.create(course=course,**branch)
            
        return course