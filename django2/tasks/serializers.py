from rest_framework import serializers
from tasks.models import Category,Branch,Contact,Course

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BranchSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Branch
        fields = ('latitude', 'longtitude', 'addreaa')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')

class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = CategorySerializer(many=False)
    class Meta:
        model = Course
        fields = ('name', 'logo', 'description', 'category', 'contacts', 'branches')

    def create(self, validated_data):
        contact=validated_data.pop('contacts')
        branch=validated_data.pop('branches')
        category=validated_data.pop('category')
        course=Course.objects.create(**validated_data)
        Contact.objects.create(course=course,**contact)
        Branch.objects.create(course=course,**branch)
        Category.objects.create(course=course,**category)
        return course