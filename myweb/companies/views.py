from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializer import stockserializer


#list all stocks or create a new one
#stocks/

class stocklist(APIView):

    def get(self, request):
        stocks = stock.objects.all()
        serializer = stockserializer(stocks, many=True)
        return Response(serializer.data)

    def post(self,request):
        stocks = stockserializer.create(self, request)
        fields = '__all__'
        serializer = stockserializer(stocks, many=True)
        return Response(serializer.data)
