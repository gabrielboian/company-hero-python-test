from django.urls import path

from .views import CompanyView, ListCompanyUsersView

urlpatterns = [
    path('', CompanyView.as_view()),
    path('users', ListCompanyUsersView.as_view())
]