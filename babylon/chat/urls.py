from django.urls import path
from . import views
from chat.views import test_routes

# Defina o namespace do app
app_name = 'chat'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('chat/', views.chat_room, name='chat'),
    path('send/', views.send_message, name='send_message'),
    path("test_routes/", test_routes),
]