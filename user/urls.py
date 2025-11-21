from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('promote-me-to-admin/', views.promote_to_admin, name='promote_to_admin'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/edit/<int:user_id>/', views.admin_edit_user, name='admin_edit_user'),
    path('admin/delete/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
]
