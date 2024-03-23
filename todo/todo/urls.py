"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from task import views
from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),

    path('home/', views.home, name='home'),
    path('homestudent/', views.homestudent, name='homestudent'),

    path('to_display', views.to_display, name='to_display'),

    path('create/', views.create_todo, name='create'),
    path('createstud/', views.createstud, name='createstud'),

    path('edit/<int:pk>/', views.edit_todo, name='edit'),

    path('editsutd/<int:pk>/', views.editsutd, name='editsutd'),

    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),

    path('deletestud/<int:pk>/', views.deletestud, name='deletestud'),

    path('completed/', views.completed, name='completed'),
    path('paginate/', views.paginate, name='paginate'),

    path('post_list/', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    ################BLOG######################

    path('Bloghome/', views.Bloghome, name='Bloghome'),
    path('Blogcreate/', views.Blogcreate, name='Blogcreate'),
    path('Blogregister/', views.Blogregister, name='Blogregister'),
    path('Bloglogin/', views.Bloglogin, name='Bloglogin'),

    path('blogedit/<int:pk>/', views.blogedit, name='blogedit'),

    path('blogdelete/<int:pk>/', views.blogdelete, name='blogdelete'),
    path('bloglogout/', views.bloglogout, name='bloglogout'),

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)