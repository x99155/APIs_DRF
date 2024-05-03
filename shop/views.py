from rest_framework.views import APIView
from rest_framework.response import Response
 
from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer
 
class CategoryAPIView(APIView):

    # defini la methode GET
    def get(self, *args, **kwargs):
        # recupère toutes les catégories
        categories = Category.objects.all() 

        # sérialise les données à l'aide de notre sérializers
        # le paramètre "many" permet de généer une liste d élément, si on veut juste sérializer un élément, alors on omet se paramètre
        serializer = CategorySerializer(categories, many=True) 

        return Response(serializer.data) # renvoi une réponse qui contient les données sérialisés
    


class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        # recup les produits
        products = Product.objects.all()

        # serialise les données
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)