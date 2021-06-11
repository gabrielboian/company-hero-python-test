from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Company

from users.models import User

class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        error_messages={'required': 'Você precisa inserir um nome para a empresa'},
        validators=[UniqueValidator(queryset=Company.objects.all(), message='Uma empresa com esse nome já existe')]
        )
    
    class Meta:
        model = Company
        fields = ('id','cnpj', 'name')

    def create(self, validated_data):
        company = super(CompanySerializer, self).create(validated_data)
        company.save()
        return company
    
class UserCompanyListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'date_joined')
    
class ListCompanyUsersSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    
    class Meta:
        model = Company
        fields = ('name', 'users')
        
    def get_users(self, instance):
        return UserCompanyListSerializer(User.objects.filter(companies=instance.id), many=True).data