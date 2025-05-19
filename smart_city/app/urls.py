from django.urls import path
from .views import * 

urlpatterns = [
    path('saveExcel/', TesteExcel.as_view()), 
    path('saveUmidade/', TesteExcel2.as_view()),
    path('saveLumi/', TesteExcel3.as_view()),
    path('saveCont/', TesteExcel4.as_view()),
    path('saveAmbi/', TesteExcel5.as_view()),
    path('listAmbi',ViewsAmbiente.as_view()),
    path('list/', ViewList.as_view())
]