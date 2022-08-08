"""
URL mappings for the user API.
"""
from django.urls import path, include

from usersapp import views
from djoser import views as DjoserViews

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'user'

urlpatterns = [
    # path('create/', views.CreateUserView.as_view(), name='create'),
    # path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),

    ### JWT ###



    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authDjoser/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/logout', DjoserViews.TokenDestroyView.as_view(), name='logout'),
]
