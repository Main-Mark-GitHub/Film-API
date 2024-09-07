from .hasher import make_password
from rest_framework.response import Response

from .models import User
from rest_framework import serializers


class FilmSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    genre = serializers.CharField(max_length=30)
    studio = serializers.CharField(max_length=30)
    score = serializers.IntegerField()


class UserSerializer(serializers.Serializer):
    mail = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        for el in User.objects.values_list('mail'):
            if el[0] == validated_data['mail']:
                return Response({"detail": "invalid mail adress", "error": "true"})

        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return Response({"detail": f"{user.mail}", "error": "false"})

    def destroy(self, instance):
        try:
            instance.delete()
            return Response({"detail": "deleted", "error": "false"})
        except Exception as e:
            return Response({"detail": "not correct data", "error": "true"})
