from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path(r'logout/', views.logout_view, name='logout'),
]
