from django.urls import path

from .views import UserView, ListCompaniesByUserView

urlpatterns = [
    path('', UserView.as_view()),
    path('list-companies/<email>', ListCompaniesByUserView.as_view()),
]