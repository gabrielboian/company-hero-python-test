from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from .serializers import CompanySerializer, ListCompanyUsersSerializer
from .models import Company

@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([AllowAny])
class CompanyView(APIView):
    queryset = Company.objects.all()
    serializer = CompanySerializer
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                context = {
                    'message': 'Empresa criada com sucesso',
                    'company': serializer.data,
                    'success': True
                }
                return Response(context, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                # A GOOD THING TO DO IS SAVE THIS EXCEPTION INTO A DB TO GET INFOS WHEN SOMETHING GET WRONG
                context = {
                    'message': 'Não foi possível criar a empresa',
                    'error': "Houve um erro inesperado em nosso servidor",
                    'success': False
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
        context = {
            'success': False,
            'error': serializer.errors
        }  
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.serializer(Company.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # A GOOD THING TO DO IS SAVE THIS EXCEPTION INTO A DB TO GET INFOS WHEN SOMETHING GET WRONG
            context = {
                'success' : False,
                'error': 'Houve um erro inesperado no servidor'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
class ListCompanyUsersView(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            queryset = Company.objects.filter(name=request.query_params['company'])
            if queryset.exists():
                serializer = ListCompanyUsersSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            context = {
                'success': False,
                'error': 'Empresa informada não existe'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # A GOOD THING TO DO IS SAVE THIS EXCEPTION INTO A DB TO GET INFOS WHEN SOMETHING GET WRONG
            context = {
                'success': False,
                'error': 'Houve um erro inesperado em nosso servidor'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)