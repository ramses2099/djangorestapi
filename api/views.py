from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Movie
from .serializers import MovieSerializer

class MovieListAV(APIView):
    """
    List movie, or create new movie
    """
    def get(self, request):
        """
        Get all movies
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        """
        Create new movie
        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

               
class MovieDetailsAV(APIView):
    
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)