from rest_framework.serializers import ModelSerializer
 
from shop.models import Category, Product

# le serializer tranforment nos données en un autre format exploitable par notre API
 
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category']