from django.urls import path
from .views import RegisterView,RegisterFromCSVView, isAuthenticated,CreateEventView, DeleteEventView,LoginView, UserView, LogoutView, EventView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegisterView.as_view()),
    path('register_from_csv', RegisterFromCSVView().as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('events', EventView.as_view()),
    path('create_event', CreateEventView.as_view()),
    path('delete_event/<int:event_id>/', DeleteEventView.as_view()),
    path('isAuthenticated', isAuthenticated().as_view()),



]