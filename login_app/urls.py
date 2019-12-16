from django.urls import path
from django.contrib.auth import views as auth


urlpatterns = [
    path(
        'login/',
        auth.LoginView.as_view(
            template_name='login_app/login.html'
        ),
        name='login'),
    path(
        'logout/',
        auth.LogoutView.as_view(),
        name='logout'
    )
]