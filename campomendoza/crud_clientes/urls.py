from django.urls import path
from . import views
from django.conf import settings
# app_name = "crud_clientes"

# app_name = "crud_clientes"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("",views.home,name="home"),
    path("crud_clientes/all/",views.all,name="all"),
    path("crud_clientes/create/",views.create,name="create"),
    path("crud_clientes/delete/<int:pk>/",views.delete,name="delete"),
    path("crud_clientes/update/<int:pk>/",views.update,name="update"),

]
