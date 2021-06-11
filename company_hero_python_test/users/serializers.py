from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

from companies.models import Company
from companies.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True, error_messages={'required': 'Você precisa inserir uma senha'})
    email = serializers.EmailField(
        required=True,
        error_messages={'required': 'Você precisa inserir um email'},
        validators=[UniqueValidator(queryset=User.objects.all(), message='Um usuário com esse e-mail já existe')]
        )
        
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'companies')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    companies = serializers.CharField()
    
    def validate(self, data):
        if not Company.objects.filter(name=data.get('companies')):
            raise serializers.ValidationError({
                'error': 'Empresa não existe em nosso banco de dados'
            })
        return data
    
    class Meta:
        model = User
        fields = ('email', 'companies')
    
    @transaction.atomic
    def update(self, instance, validated_data):
        company = Company.objects.get(name=validated_data.get('companies'))
        instance.companies.add(company.id)
        instance.save()
        return validated_data
    
class ListCompaniesByUserSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'companies')