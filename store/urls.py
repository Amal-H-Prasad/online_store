from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('checkout', views.profile, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('admin_home', views.admin_home, name="admin_home"),
    path('user_home', views.user_home, name="user_name"),
    path('passwordchange', views.passwordchange, name="passwordchange"),
    path('forgetpassword', views.forgetpassword, name="forgetpassword"),
    path('logout_view', views.logout_view, name='logout_view'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('admin_view_user',views.admin_view_user,name='admin_view_user'),
    path('edituser/<id>', views.edituser, name='edituser'),
    path('edituser1', views.edituser1, name='edituser1'),
    path('deleteuser/<id>', views.deleteuser, name='deleteuser'),
    # path('deleteuser1', views.deleteuser1, name='deleteuser1')
    path('user_add_review',views.user_add_review,name='user_add_review'),


]
