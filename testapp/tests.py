
from rest_framework.test import APITestCase
from testapp.models import Employ

# # Create your tests here.
# class EmployeTestcase(TestCase):
#     def setup(self):
#         print('this is test case setup only')
#         Employ.objects.create(eno=107,ename='sravs',esal=300,eadress='hyd')
#         Employ.objects.create(eno=108,ename='sravani',esal=500,eadress='mubai')
        
#     def test_employ_info(self):
#         print('testing employ info')
#         qs=Employ.objects.all()
#         self.assertEqual(qs.count(),2)
#         e1=Employ.objects.get(ename='sravs')
#         e2=Employ.objects.get(ename='sravani')
#         self.assertEqual(e1.get_sal(),300)
#         self.assertEqual(e2.get_sal(),50)
                                                    
class EmployeAPITestcase(APITestCase):
    def setUp(self):
        print('this is test case setup only')
        Employ.objects.create(eno=1222,ename='sravs',esal=3000,eadress='hyd')
    def test_get_method(self):
        url='http://127.0.0.1:8000/api/' 
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)  
        qs=Employ.objects.filter(ename='sravs')
        self.assertEqual(qs.count(),1)
        print('the succus are not',response.status_code)