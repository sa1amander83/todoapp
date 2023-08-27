"""
URL configuration for todoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from todo.views import LoginUser, Profile, Register, edittodo, deltodo, AddTodo, addtodo, update_status, logout_user, \
    page_not_found_view
from todoapp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginUser.as_view(), name='login' ),
    path(r'profile/<slug:todo_user>/', Profile.as_view(),name='profile' ),
    path('register/',Register.as_view(), name='register' ),
    # path('/profile/<slug:todo_user>/add/',addtodo,name='addtodo' ),
    path('profile/<slug:todo_user>/add/', AddTodo.as_view(),name='addtodo' ),
    path('profile/<slug:todo_user>/update/', update_status,name='update' ),

    path('profile/<slug:todo_user>/edit/<int:todo_id>/',edittodo,name='edittodo' ),
    path('profile/<slug:todo_user>/delete/<int:todo_id>/',deltodo,name='deltodo' ),
    path('logout/',logout_user,name='logout' ),
    # path('', ),
]


handler404 = page_not_found_view