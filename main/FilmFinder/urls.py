from django.urls import path
from .views import UserApiRegister, UserApiDelete, FilmApiView

urlpatterns = [
    path("API/v1/registration", UserApiRegister.as_view()),
    path("API/v1/films", FilmApiView.as_view()),
    path("API/v1/delete", UserApiDelete.as_view()),


]
