from django.urls import path
from .views import * 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title='Smart City',
        default_version='v0.1',
        description='API Documentation for Project.', 
    ), 
    public=True,
    permission_classes=(permissions.AllowAny,),
)
    
    

urlpatterns = [
    path("teste/", DetailUpdateDeleteAmbiente.as_view()),


    path('saveA/', SaveAmbiente.as_view()),
    path('saveL/', SaveLuminosidade.as_view()),
    path('saveC/', SaveContador.as_view()),
    path('saveU/', SaveUmidade.as_view()),
    path('saveT/', SaveTemperatura.as_view()),
    path('saveH/', SaveHistorico.as_view()),
    path("listSS/", CreateListAmbiente.as_view(), ),
    # path('importar/', ImportExcelData.as_view(), name='importar-dados'),
    path('exportH/', ExportHistorico.as_view()),
    path('exportS/', ExportSensores.as_view()),
    path('exportA/', ExportAmbientes.as_view()),

    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('criar/', CreateUserView.as_view()),

    path('redoc/', view=schema_view.with_ui('redoc', cache_timeout=0)), # --> Com redoc 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # --> Com Swaager
]


