from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),  # Tela inicial é a de registro
    path('login/', views.user_login, name='login'),  # Tela de login
    path('chat/', views.chat_room, name='chat'),  # Tela do chat
    path('', include('chat.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]