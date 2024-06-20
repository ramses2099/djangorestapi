from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer

class WatchListAV(APIView):
    """
    List movie, or create new movie
    """
    def get(self, request):
        """
        Get all movies
        """
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        """
        Create new movie
        """
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              
class WatchDetailsAV(APIView):
    
    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        watchlist = self.get_object(pk=pk)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        watchlist = self.get_object(pk=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        watchlist = self.get_object(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatformListAV(APIView):
    def get(self, request):
        streamplatform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamplatform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailsAV(APIView):
    
    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        streamplatform = self.get_object(pk=pk)
        serializer = StreamPlatformSerializer(streamplatform)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        streamplatform = self.get_object(pk=pk)
        serializer = StreamPlatformSerializer(streamplatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        streamplatform = self.get_object(pk=pk)
        streamplatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
