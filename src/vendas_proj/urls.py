from django.contrib import admin
from django.urls import path
from vendas import views

# Define a url que vai ser chamada na nossa função view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('http://localhost:8080/', views.index, name='index'),
]
