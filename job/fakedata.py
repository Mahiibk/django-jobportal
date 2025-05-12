import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job.settings')  # ✅ Corrected spelling

import django
django.setup()

from testapp.models import Hydjobs
from faker import Faker
from random import *

fake = Faker()

def phonenubmer():
    d1 = randint(6, 9)
    num = '' + str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)

def fakeRecord(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project_manager', 'team lead', 'software engineer', 'Associate engineer', 'FSD', 'trainer'))
        feligiblity = fake.random_element(elements=('b tech', "BCA", 'MCA', "MBA", "BBA"))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenubmer()

        Hydjobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligiblity=feligiblity,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )

n = int(input("Enter number of records: "))
fakeRecord(n)
print(f'{n} records inserted')
