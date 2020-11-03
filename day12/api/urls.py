from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


from api import views

urlpatterns = [
    # 签发token 登录逻辑
    path('login/',obtain_jwt_token),

    # 访问需要认证 在认证
    path('detail/',views.UserDetailAPIView.as_view()),

#     自定义签发token
    path('user/', views.LoginAPIView.as_view()),


    path('com/', views.ComputerListAPIView.as_view()),



]
