from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
     path('contact/', views.contact, name='contact'),
    path('addpost/',views.add_post,name='addpost'),
   path('updatepost/<int:id>',views.update_post,name='updatepost'),
   path('deletepost/<int:id>',views.delete_post,name='deletepost'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)