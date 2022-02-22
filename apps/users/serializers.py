from dataclasses import field
from rest_framework import serializers

from apps.users.models import User,Film,UserMovie

class FilmSerializer(serializers.ModelSerializer):
    view_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Film
        fields = ('id','title', 'view_count')
    
    def get_view_count(self, obj):
        return UserMovie.objects.filter(movie__id=obj.id).count()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username','password')

    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user

class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class UserMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMovie
        fields = '__all__'

# class RecomendationSerializer(serializers.Serializer):
#     film = serializers.CharField(read_only=True)

#     class Meta:
#         fields = '__all__'
