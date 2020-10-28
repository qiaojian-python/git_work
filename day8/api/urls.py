
from django.urls import path

from api import views

urlpatterns = [
    path('student/',views.StudentAPIView.as_view()),
    path('student/<str:id>/',views.StudentAPIView.as_view()),

    path('teacher/',views.TeacherAPIView.as_view()),
    path('teacher/<str:id>/',views.TeacherAPIView.as_view()),
]
