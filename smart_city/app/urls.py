from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('saveExcel/', TesteExcel.as_view()), 
    path('saveUmidade/', TesteExcel2.as_view()),
    path('saveLumi/', TesteExcel3.as_view()),
    path('saveCont/', TesteExcel4.as_view()),
    path('saveAmbi/', TesteExcel5.as_view()),
    path('listAmbi',ViewsAmbiente.as_view()),
    path('list/', ViewList.as_view()),

    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('criar/', CreateUserView.as_view()),
]