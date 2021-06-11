from django.urls import path

urlpatterns = [
    path('', CompanyView.as_view()),
    path('users', ListCompanyUsersView.as_view())
]