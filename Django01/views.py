from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Test
from .serializers import TestSerializer

class TestListApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''

        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
