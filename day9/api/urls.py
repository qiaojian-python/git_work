
from django.urls import path

from api import views

urlpatterns = [
    path('book/',views.BookAPIView.as_view()),
    path('book/<str:id>/',views.BookAPIView.as_view()),

    # 整合版本
    path('v2/book/', views.BookAPIViewV2.as_view()),
    path('v2/book/<str:id>/', views.BookAPIViewV2.as_view()),
]




