from django.urls import path
from .views import HomePageView, SnackListView, SnackDetailView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', SnackListView.as_view(), name='snack_list'),
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
]
