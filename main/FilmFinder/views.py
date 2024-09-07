from rest_framework.views import APIView
from .serializers import *
from .models import Film, User

# Create your views here.


class FilmApiView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data

            obj = User.objects.filter(mail=data["mail"])[0]

            if obj.password == make_password(data["password"]):
                queryset = Film.objects.all()
                serializer = FilmSerializer(queryset, many=True)
                return Response({"detail": serializer.data, "error": "false"})

            return Response({"detail": "not accept account", "error": "true"})

        except Exception:
            return Response({"detail": "not correct data", "error": "true"}) 


class UserApiRegister(APIView):
        @staticmethod
        def post(request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                return serializer.save()
            return Response(serializer.errors)


class UserApiDelete(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            obj = User.objects.filter(mail=data['mail'])[0]
            if obj.password == make_password(data["password"]):
                serializer = UserSerializer(data=obj)

                return serializer.destroy(obj)
            return Response({"detail": "not correct data", "error": "true"})
        except Exception:
            return Response({"detail": "not correct data", "error": "true"})
