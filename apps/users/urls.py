from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.users import views

router = DefaultRouter()
router.register('user', views.UserView,basename='user_api')
router.register('film', views.FilmView,basename='film_api')
router.register('user-movie', views.UserMovieView,basename='user-movie_api')

urlpatterns = [
    path('current', views.current_user, name='current_user'),
    path('recomendations/', views.RecomendationAPIView.as_view(), name='recomendations')
]
urlpatterns += router.urls