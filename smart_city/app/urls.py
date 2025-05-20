from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('saveAmbi/', SaveAmbiente.as_view()),
    path('saveLumi/', SaveLuminosidade.as_view()),
    path('saveCont/', SaveContador.as_view()),
    path('saveUmi/', SaveUmidade.as_view()),
    path('saveTemp/', SaveTemperatura.as_view()),
    path('saveHistUmi/', SaveHistoricoUmidade.as_view()),
    path('listAmbi',ViewsAmbiente.as_view()),
    path('list/', ViewList.as_view()),

    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('criar/', CreateUserView.as_view()),
]