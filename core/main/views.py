from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

class CarAPIView(APIView):
    def get(self, request):
        c = Car.objects.all()
        return Response({'cars':CarSerializer(c, many=True).data})

    def post(self, request):
        post_new = Car.objects.create(
            name=request.data['name'],
            about=request.data['about'],
            price=request.data['price'],
            category_id=request.data['category_id']
        )
        return Response({'post':CarSerializer(post_new).data})
