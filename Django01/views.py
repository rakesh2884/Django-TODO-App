from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Test
from .serializers import TestSerializer

class TestListApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TestDetailApiView(APIView):
    def get(self,request,id):
        test=get_object_or_404(Test,id=id)
        serializer=TestSerializer(test)
        return Response(serializer.data)
    def delete(self, request, id):
        test=get_object_or_404(Test,id=id)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request,id):
        test=get_object_or_404(Test, id=id)
        serializer=TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)