
from django.urls import path

from api import views

urlpatterns = [
    path('book/',views.BookAPIView.as_view()),
    path('book/<str:id>/',views.BookAPIView.as_view()),

    # 整合版本
    path('v2/book/', views.BookAPIViewV2.as_view()),
    path('v2/book/<str:id>/', views.BookAPIViewV2.as_view()),

#     genericview
    path('gen/', views.BookGenericAPIView.as_view()),
    path('gen/<str:id>/', views.BookGenericAPIView.as_view()),

#     genericview2
    path('gentool/', views.BookGenericAPIView2.as_view()),
    path('gentool/<str:id>/', views.BookGenericAPIView2.as_view()),

#     setview
    path('set/', views.BookViewSetView.as_view({'get':"get_user_count",'post':'user_login'})),
    path('set/<str:id>/', views.BookViewSetView.as_view({'get':"get_user_count",'post':'user_login'})),

#  作业set_view
    path('userset/', views.UserViewSetView.as_view({'get': "get_user_count"})),
    path('userset/login/', views.UserViewSetView.as_view({'post': 'user_login'})),
    path('userset/regist/', views.UserViewSetView.as_view({'post': 'user_regist'})),
    path('userset/<str:id>/', views.UserViewSetView.as_view({'get': "get_user_count"})),
# 两个类视图解决post冲突 regist分离
]



