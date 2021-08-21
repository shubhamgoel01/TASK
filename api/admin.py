from django.contrib import admin
from api.models import MobileCompany, Customer
from api.serializers import MobileCompanySerializer,CustomerSerializer

admin.site.register(MobileCompany)
admin.site.register(Customer)