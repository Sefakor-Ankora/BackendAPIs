from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from register.models import Register
from register.serializers import Register
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from .serializers import RegisterSerializer
from events.serializers import EventsSerializer


class Register(generics.ListCreateAPIView):
    # get method handler
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    
#Count the total number of registered events
 
class RegisterCountView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

def get(self,request,format = None):
        events = Register.objects.all()
        count = events.__len__()
        serializer = RegisterSerializer(event,many = True)
        return Response({"count":count, "data":serializer.data})
        
        



# Create your views here.
#@api_view(['GET','POST'])
#def register_list(request):
 #   if request.method == 'GET':
  #      register = Register.objects.all()
#
 #       name = request.GET.get('name', None)
  #      if name is not None:
   #         register = register.filter(name_icontains=name)
#
 #       register_serializer = RegisterSerializer(register, many=true)
  #      return JsonResponse(register_serializer.data, safe=False)
   #     #safe=false for object serialization

    #elif request.method == 'POST':
     #       register_data = JSONParser().parse(request)
      #      register_serializer = RegisterSerializer(data=register_data)
       #     if register_serializer.is_valid():
        #        register_serializer.save()
         #       return JsonResponse(register_serializer.data, status=status.HTTP_201_CREATED)
          #  return JsonResponse(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)






#@api_view(['GET', 'PUT', 'DELETE'])
#def register_details(request, pk):
 #   try:
  #      register = Register.objects.get(pk=pk)
   # except Register.DoesNotExist:
    #    return JsonResponse({'message': 'The Event does not exist'},status=status.HTTP_404_NOT_FOUND)

    #if request.method =='GET':
     #   register_serializer = RegisterSerializers(register)
      #  return JsonResponse(register_serializer.data)
    
    #elif request.method == "PUT":
     #   register_data = JSONParser().parse(request)
      #  register_serializer = RegisterSerializer(register, data=register_data)
       # if register_serializer.is_valid():
        #        register_serializer.save()
         #       return JsonResponse(register_serializer.data)
          #      return JsonResponse(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #elif request.method == 'DELETE':
     #   register.delete()
      #  return JsonResponse({'message': 'Event was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


