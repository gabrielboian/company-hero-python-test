from django.urls import path, include

urlpatterns = [
    path('api/users/', include('users.urls')),
    path('api/company/', include('companies.urls')),
]
