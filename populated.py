import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','withrest1.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
faker=Faker()
def populated(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,200000)
        feadres=faker.city()
        emp_record=Employ.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eadress=feadres)
        
populated(120)        