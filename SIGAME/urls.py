from django.contrib import admin
from django.urls import path
from apps.cliente import views as clienteViews

urlpatterns = [
  #========================================================================================== ADMIN
  path('admin/', admin.site.urls),
  
  
  #=========================================================================================== HOME
  path('', clienteViews.home),
  
  #======================================================================================== CLIENTE

  
  #======================================================================================= RESTRITO

]
