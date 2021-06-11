from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, UserUpdateSerializer, ListCompaniesByUserSerializer
from .models import User

@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([AllowAny])
# PERMISSION TO ANY PERSON COULD BE REGISTER YOURSELF
class UserView(APIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer = UserSerializer
    
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        serializer = self.serializer(User.objects.all(), many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                context = {
                    'message': 'Usuário criado com sucesso',
                    'user': serializer.data,
                    'success': True
                }
                return Response(context, status=status.HTTP_201_CREATED)
            except Exception as e:
                # A GOOD THING TO DO IS SAVE THIS EXCEPTION INTO A DB TO GET INFOS WHEN SOMETHING GET WRONG
                context = {
                    'error': 'Não foi possível criar o usuário',
                    'success': False
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
        context = {
            'success': False,
            'error': serializer.errors
        }  
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.data['email'])
            serializer = UserUpdateSerializer(user, data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # A GOOD THING TO DO IS SAVE THIS EXCEPTION INTO A DB TO GET INFOS WHEN SOMETHING GET WRONG
            context = {
                'success': False,
                'error': 'Houve um erro inesperado em nosso servidor'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
    
class ListCompaniesByUserView(APIView):
    
    @csrf_exempt
    def get(self, request, email, *args, **kwargs):
        try:
            queryset = User.objects.filter(email=email)
            if queryset.exists():
                serializer = ListCompaniesByUserSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            context = {
                'success': False,
                'error': 'Não foi possível encontrar os dados com o usuário informado'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # A GOOD THING TO DO IS SAVE THIS EXCEPTION INTO A DB TO GET INFOS WHEN SOMETHING GET WRONG
            context = {
                'success': False,
                'error': 'Houve um erro inesperado em nosso servidor'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)