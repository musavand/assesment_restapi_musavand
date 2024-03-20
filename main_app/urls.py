from django.urls import path
from .views import home,get_data,say_hello

urlpatterns = [
    path("", home, name="home"),
    path("get_data",get_data,name="get_data"),
    path("say_hello",say_hello ,name ="say_hello")
]
