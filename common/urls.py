from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.ProfileView, name='profile'),
    path('recheck/<int:pk>/', views.recheck, name='recheck'),
]

# re_path(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name='profile'),