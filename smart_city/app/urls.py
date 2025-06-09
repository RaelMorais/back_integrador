from django.urls import path
from .views import * 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

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
    #Ambientes Paths
    path("ambiente/", AmbienteView.as_view()),
    path("ambiente/<int:pk>", AmbienteView.as_view()),
    path("import/ambiente/", ImportAmbienteData.as_view()),
    path("export/ambiente/", ExportAmbientes.as_view()), 

    #Sensores Paths 
    path("sensores/", SensoresView.as_view()), 
    path("sensores/<int:pk>/", SensoresView.as_view()), 
    path("import/sensores/contador/", ImportContador.as_view()), 
    path("import/sensores/luminosidade/", ImportLuminosidade.as_view()),
    path("import/sensores/umidade/", ImportUmidade.as_view()),
    path("import/sensores/temperatura/", ImportTemperatura.as_view()),  
    path("export/sensores/", ExportSensores.as_view()), 

    #Historico Paths 
    path("historico/", HistoricoView.as_view()),
    path("historico/<int:pk>", HistoricoView.as_view()),
    path("import/historico/", ImportHistorico.as_view()),
    path("export/historico/", ExportHistorico.as_view(),), 

    #Obtain Token 
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path("user/import/", SaveUser.as_view()),
    #Create User 
    path('user/create/', CreateUserView.as_view()),

    #Swagger & Redoc
    path('redoc/', view=schema_view.with_ui('redoc', cache_timeout=0)), # --> Com redoc 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # --> Com Swaager
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


