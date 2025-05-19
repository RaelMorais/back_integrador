from django.shortcuts import render
from .permissions import * 
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import * 
from openpyxl import load_workbook
from django.conf import settings
import os
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

def parse_float(val):
    if isinstance(val, str):
        val = val.replace(',', '.')
    try:
        return float(val)
    except:
        return None

class TesteExcel(APIView):
    permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'luminosidade.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for linha_planilha, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sensor, mac, unidade, valor, lat, lon, status_valor, timestamp = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'valor': parse_float(valor),
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                        'timestamp': timestamp
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# umidade.xlsx
class TesteExcel2(APIView):
    permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'temperatura.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for linha_planilha, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sensor, mac, unidade, valor, lat, lon, status_valor, timestamp = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'valor': parse_float(valor),
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                        'timestamp': timestamp
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TesteExcel3(APIView):
    permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'umidade.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for linha_planilha, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sensor, mac, unidade, valor, lat, lon, status_valor, timestamp = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'valor': parse_float(valor),
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                        'timestamp': timestamp
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   


class TesteExcel4(APIView):
    permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'contador.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for linha_planilha, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sensor, mac, unidade, valor, lat, lon, status_valor, timestamp = row

                sensor_data = {
                        'sensor': sensor,
                        'mac_address': mac,
                        'unidade_medida': unidade,
                        'valor': parse_float(valor),
                        'latitude': parse_float(lat),
                        'longitude': parse_float(lon),
                        'status': status_valor,
                        'timestamp': timestamp
                    }

                serializer = SensoresSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

class TesteExcel5(APIView):
    permission_classes =[IsDirector]
    def post(self, request):
        caminho_arquivo = os.path.join(settings.BASE_DIR, '..', 'Dados Integrador', 'ambientes.xlsx')

        try:
            wb = load_workbook(caminho_arquivo, data_only=True)
            sheet = wb.active

           
            for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                if not any(row):
                    continue

                sig, descricao, ni, responsavel = row

                sensor_data = {
                        'sig': sig,
                        'descricao':descricao,
                        'ni':ni, 
                        'responsavel':responsavel
                    }

                serializer = AmbienteSerializer(data=sensor_data)
                if serializer.is_valid():
                    serializer.save()
            return Response({'mensagem': 'Importação concluída'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)      


class ViewList(ListAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes =[IsDirectorOrProfessor]

class ViewsAmbiente(ListAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes =[IsDirectorOrProfessor]

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class CreateUserView(APIView):
    permission_classes = [IsDirector]
    def post(self, request):
        if not request.user.has_perm('app.add_usuario'):  
            return Response({"detail": "Você não tem permissão para criar usuários."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            return Response({
                'message':"usuario criado"
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
