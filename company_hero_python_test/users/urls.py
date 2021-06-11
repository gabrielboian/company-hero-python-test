from django.urls import path

urlpatterns = [
    path('', UserView.as_view()),
    path('list-companies/<email>', ListCompaniesByUserView.as_view()),
]