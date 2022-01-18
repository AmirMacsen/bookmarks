from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),

    # 重置密码
    path("password_change", auth_view.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_view.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", auth_view.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # 用户注册
    path('register/', views.register, name="register"),

    # 用户编辑
    path("edit/", views.edit, name="edit"),

    # 用户关注
    path('users/follow/',views.user_follow, name="user_follow"),

    # 用户列表和详情
    path("users/", views.user_list, name="user_list"),
    path("users/<username>", views.user_detail, name="user_detail"),


]
