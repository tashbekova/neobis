from rest_framework import serializers
from tasks.models import Category,Branch,Contact,Course

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','imgpath')

  class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longtitude', 'addreaa')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TaskSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Course
        fields = ('name', 'category', 'description', 'contacts', 'logo', 'branches')

