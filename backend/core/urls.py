from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('socialaccounts/', views.socialaccount_list, name='socialaccount_list'),
    path('socialaccounts/create/', views.socialaccount_create, name='socialaccount_create'),
    path('socialaccounts/<int:pk>/edit/', views.socialaccount_edit, name='socialaccount_edit'),
    path('socialaccounts/<int:pk>/delete/', views.socialaccount_delete, name='socialaccount_delete'),
    path('scheduledposts/', views.scheduledpost_list, name='scheduledpost_list'),
    path('scheduledposts/create/', views.scheduledpost_create, name='scheduledpost_create'),
    path('scheduledposts/<int:pk>/edit/', views.scheduledpost_edit, name='scheduledpost_edit'),
    path('scheduledposts/<int:pk>/delete/', views.scheduledpost_delete, name='scheduledpost_delete'),
    path('analyticses/', views.analytics_list, name='analytics_list'),
    path('analyticses/create/', views.analytics_create, name='analytics_create'),
    path('analyticses/<int:pk>/edit/', views.analytics_edit, name='analytics_edit'),
    path('analyticses/<int:pk>/delete/', views.analytics_delete, name='analytics_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
