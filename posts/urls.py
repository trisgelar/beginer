from django.urls import path

from .views import HomePostPageView

urlpatterns = [
	path('', HomePostPageView.as_view(), name='home_post'),
]