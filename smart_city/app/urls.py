from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('saveA/', SaveAmbiente.as_view()),
    path('saveL/', SaveLuminosidade.as_view()),
    path('saveC/', SaveContador.as_view()),
    path('saveU/', SaveUmidade.as_view()),
    path('saveT/', SaveTemperatura.as_view()),
    path('saveH/', SaveHistorico.as_view()),
    path('listAmbi',ViewsAmbiente.as_view()),
    path('list/', ViewList.as_view()),
    path('listH/', viewHistorico.as_view()),

    path('exportH/', ExportHistorico.as_view()),
    path('exportS/', ExportSensores.as_view()),
    path('exportA/', ExportAmbientes.as_view()),

    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('criar/', CreateUserView.as_view()),
]