from django.urls import path

from . import views

urlpatterns = [
    path("", views.DinosaurView.as_view()),
    path("<int:pk>/", views.DinosaurDeleteView.as_view()),
    path("media/", views.DinosaurMediaCreateView.as_view()),
    path("media/<int:pk>/", views.DinosaurMediaDeleteView.as_view()),
    path("<int:pk>/like/", views.DinosaurLikeView.as_view()),
]
