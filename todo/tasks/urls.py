from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.home_view ,name ='home'),
    path('create/',views.create_view, name='create'),
    path('<int:pk>',views.delete_view, name='delete')
]
