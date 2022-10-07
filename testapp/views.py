from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import EmployeSerilaizers
from testapp.models import Employ
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

# class EmployeeCRUDCBV(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)

class EmployApiview(APIView):
    def get(self,request,*args,**kwrgs):
        clours=['red','green']
        return Response({'msg':'these are get','colours':clours})
    def post(self,request,*args,**kwrgs):
        serilizers=EmployeSerilaizers(data=request.data)
        if serilizers.is_valid():
            name=serilizers.data.get('ename')
            msg='hellow {}'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serilizers.errors,status=400)
from rest_framework.viewsets import ViewSet,ModelViewSet          
class  TestViewset(ViewSet):
    def list(self,request):
        clours=['red','green']
        return Response({'msg':'these are get','colours':clours})
    def create(self,request,*args,**kwrgs):
        serilizers=EmployeSerilaizers(data=request.data)
        if serilizers.is_valid():
            name=serilizers.data.get('ename')
            msg='hellow {}'.format(name)
            return Response({'msg':msg})   
        else:
            return Response(serilizers.errors,status=400)
        
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated   
from testapp.authentications import CustomAuthenticate     
from testapp.pagination import *
class  TestViewset1(ModelViewSet):
    queryset=Employ.objects.all()
    serializer_class=EmployeSerilaizers
    pagination_class=Mypagination3
    #authentication_classes=[CustomAuthenticate]
    #permission_classes=[IsAuthenticated,]
          
        
# class EmpAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employ.objects.all()
#         serializers=EmployeSerilaizers(qs,many=True)
#         return Response(serializers.data)
    
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView
class EmployListApi(ListAPIView):
    #queryset=Employ.objects.all()
    serializer_class=EmployeSerilaizers
    def get_queryset(self):
        qs=Employ.objects.all()   
        name=self.request.GET.get('xxx')
        if name is not None:
            qs=qs.filter(ename_icontains=name)
        return qs 
    
class EmployCreateApi(CreateAPIView):
    queryset=Employ.objects.all()
    serializer_class=EmployeSerilaizers    

class EmployREApi(RetrieveAPIView):
    queryset=Employ.objects.all()
    serializer_class=EmployeSerilaizers  
    lookup_field='pk'
    
class EmployUPREApi(UpdateAPIView):
    queryset=Employ.objects.all()
    serializer_class=EmployeSerilaizers  
    lookup_field='pk'    