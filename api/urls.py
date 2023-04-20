from django.urls import path
from .views import TaskView,UserView,CreateUserView

urlpatterns = [
    path('task', TaskView.as_view()),
    path('task/<int:pk>', TaskView.as_view()),
    path('user/<str:user>', UserView.as_view(), name='user-link'),
    path('user', CreateUserView.as_view()),
]
