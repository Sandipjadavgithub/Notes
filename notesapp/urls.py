from django.urls import path
from .views import*
from .import views

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('create-note/',Createnote.as_view(),name='create-note'),
    path('update-note/<int:pk>/',UpdateNote.as_view(),name='update-note'),
    path('delete-note/<int:pk>/',DeleteNote.as_view(),name='delete-note'),
    path('register',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout',views.logoutpage,name='logout'),
    
]
