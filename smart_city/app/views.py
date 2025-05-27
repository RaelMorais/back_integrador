from django.shortcuts import render
from .permissions import * 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import * 
from openpyxl import load_workbook, Workbook
from django.conf import settings
import os
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# View to http method GET and POST to Model -> Ambiente with only Director Permission 
class CreateListAmbiente(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbienteSerializer
    http_method_names = ['get', 'post']
    # permission_classes = [IsDirector]
    
    swagger_auto_schema(
        operation_description='Create a ambiente', 
        request_body=AmbienteSerializer,
        responses={
            201: openapi.Response("Successfully created Ambiente ✅", AmbienteSerializer),
            400: "Bad Request"
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully created Ambiente ✅'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Error to create Ambiente 😥'}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description='Show all ambientes',
        responses={
            200: AmbienteSerializer,
            404: 'Not Found',
        }
    )
    def get(self, request, *args, **kwargs):
        ambientes = self.get_queryset()
        serializer = self.get_serializer(ambientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DetailUpdateDeleteAmbiente(RetrieveUpdateDestroyAPIView):
    '''
    View to retrieve, update, and delete Ambiente by ID.
    '''
    queryset = Ambientes.objects.all()
    serializer_class = AmbienteSerializer
    http_method_names = ['get', 'put', 'delete']
    
    # permission_classes = [IsDirector]
    @swagger_auto_schema(
        operation_description='Show specific ambiente using ID',
        responses={
            200: AmbienteSerializer,
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        }
    )
    
    def get(self, request, *args, **kwargs):
        try:
            ambientes = self.get_object()
            serializer = self.get_serializer(ambientes)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            raise Http404('Not Found')
        
    @swagger_auto_schema(
        operation_description='Update ambiente by ID',
        request_body=AmbienteSerializer,
        responses={
            200: AmbienteSerializer,
            400: 'Bad Request',
            404: 'Not Found',
            500: 'Internal Server Error'
        }
    )

    def put(self, request, *args, **kwargs): # <-- For the update 
        try: 
            ambientes = self.get_object()
            serializer = self.get_serializer(ambientes, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Successfully ✅✨', 'data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'message':'Error processing request', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            raise Http404('Not Found')
        
    @swagger_auto_schema(
        operation_description='Delete ambiente by ID',
        responses={
            204: 'Successfully deleted',
            404: 'Not Found',
            500: 'Internal Server Error'
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            ambientes = self.get_object()
            ambientes.delete()
            return Response({'message':'Successfully ✅'}, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            raise Http404('Not Found')


































# Create your views here.
def parse_float(val):
    if isinstance(val, str):
        val = val.replace(',', '.')
    try:
        return float(val)
    except:
        return None

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class CreateUserView(APIView):
    permission_classes = [IsDirector]
    def post(self, request):
        if not request.user.has_perm('app.add_usuario'):  
            return Response({"detail": "Você não tem permissão para criar usuários."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
             
            return Response({
                'message':"usuario criado"
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################################################################################################################################IMPORT 
# Views for import data from Excel in to Database

# Save 'Ambiente' data 
class SaveAmbiente(APIView):
    # permission_classes =[IsDirector]
    def post(self, request):
        file_path = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'ambientes.xlsx')
        try:
            wb = load_workbook(file_path, data_only=True)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if not any(row):
                    continue
                sig, descricao, ni, responsavel = row # Variables in portugues to avoid mistakes

                sensor_data = {
                        'sig': sig,
                        'descricao':descricao,
                        'ni':ni, 
                        'responsavel':responsavel
                    }

                serializer = AmbienteSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'message': 'Data ''Ambiente'' imported successfully ✅'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
# Save 'Contador' data 
class SaveContador(APIView):
    # permission_classes =[IsDirector]
    def post(self, request):
        file_path = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'contador.xlsx')

        try:
            wb = load_workbook(file_path, data_only=True)
            sheet = wb.active

           
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if not any(row):
                    continue

                sensor, mac, unidade, lat, lon, status_valor = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


# Save 'Historico' data  
class SaveHistorico(APIView):
    # permission_classes = [IsDirector]
    def post(self, request):
        file_Path = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'historico.xlsx')
  
        try:
            wb = load_workbook(file_Path, data_only=True)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                sensor_id, ambiente_id, value, timestamp = row

                dados = {
                    'sensor': sensor_id,      
                    'ambiente': ambiente_id,  
                    'valor': float(value),
                    'timestamp': timestamp  
                }

                serializer = HistoricoSerializer(data=dados)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(f"Serializer Error: {serializer.errors}")

            return Response({
                'message': 'Successfully imported 😃',
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Save 'Luminosidade' data 
class SaveLuminosidade(APIView):
    # permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'luminosidade.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if not any(row):
                    continue

                sensor, mac, unidade, lat, lon, status_valor = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Save 'Temperatura'  
class SaveTemperatura(APIView):
    # permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'temperatura.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for linha_planilha, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sensor, mac, unidade, lat, lon, status_valor = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Save 'Umidade' 
class SaveUmidade(APIView):
    # permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'umidade.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for linha_planilha, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sensor, mac, unidade, lat, lon, status_valor  = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        
######################################################################################################################################EXPORT 
class ExportSensores(APIView):
    def get(self, request):
        sensores = Sensores.objects.all()

        wb = Workbook()

        ws_sensores = wb.active

        header = ['sensor','mac_address','unidade_medida','latitude','longitude','status']
        ws_sensores.append(header)

        for sensor in sensores:
            export_data = [
                sensor.sensor, 
                sensor.mac_address,
                sensor.unidade_medida, 
                sensor.latitude, 
                sensor.longitude, 
                sensor.status
            ]
            ws_sensores.append(export_data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="sensores.xlsx"'
        wb.save(response)

        return response

class ExportAmbientes(APIView):
        def get(self, request):
            ambientes = Ambientes.objects.all()

            wb = Workbook()

            ws_ambientes = wb.active

            header = ['sig','descricao','ni','responsavel']
            ws_ambientes.append(header)

            for ambiente in ambientes:
                export_data = [
                    ambiente.sig,
                    ambiente.descricao, 
                    ambiente.ni,
                    ambiente.responsavel
                ]
                ws_ambientes.append(export_data)
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="ambiente.xlsx"'
            wb.save(response)

            return response
class ExportHistorico(APIView):

    def get(self, request):
        historicos = Historico.objects.all()

        wb = Workbook()

        ws_historico = wb.active

        header = ['sensor',	'ambiente',	'valor', 'timestamp']
        ws_historico.append(header)

        for historico in historicos:
            export_data = [
                historico.sensor.sensor,
                historico.ambiente.descricao, 
                historico.valor,
                historico.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            ]
            ws_historico.append(export_data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="historico.xlsx"'
        wb.save(response)

        return response
    
