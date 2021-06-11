from django.db import models
from django.utils.translation import ugettext_lazy as _

class Company(models.Model):
    cnpj = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    users = models.ManyToManyField('users.User', _('users'), blank=False)
    
    class Meta:
        db_table = 'company'
        verbose_name = _('company')
        verbose_name_plural = _('companies')
    
    
    def get_all_users(self):
        print(self.users.name)
        return self.users.all()