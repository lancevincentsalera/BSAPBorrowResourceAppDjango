from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('resident-registration/', views.ResidentRegistration.as_view(), name='resident_registration'),
    path('organization-registration/', views.OrganizationRegistration.as_view(), name='organization_registration'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('login/', views.Login.as_view(), name="login"),
    path('resource/', views.resource_type, name="resource"),
    path('borrow/', views.Borrow.as_view(), name="borrow"),
    path('borrowed/', views.dashboard, name="borrowed"),
    path('logout/', views.Logout.as_view(), name="logout"),
]
