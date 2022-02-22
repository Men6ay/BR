from collections import Counter
from rest_framework import viewsets, views
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.models import Film,User,UserMovie
from apps.users import serializers

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.UserSerializerList
        return self.serializer_class

class UserMovieView(viewsets.ModelViewSet):
    queryset = UserMovie.objects.all()
    serializer_class = serializers.UserMovieSerializer


class UserRecomendationViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        user = request.user


class RecomendationAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        user_movies = UserMovie.objects.all()
        recomend_movies = []
        my_movies = []
        for watched in user_movies:
            if watched.user.id == user.id:
                my_movies.append(watched.movie)
                
            if watched.movie not in my_movies:
                recomend_movies.append(watched.movie.title)
        
        top_movie = Counter(recomend_movies)

        return Response(dict(top_movie), status=status.HTTP_200_OK)       

        
@api_view(['GET'])
def current_user(request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)


