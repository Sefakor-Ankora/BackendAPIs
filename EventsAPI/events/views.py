from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from events.models import Events
from events.serializers import Events
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import EventsSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets,generics,permissions



class Events(generics.ListCreateAPIView):
    # get method handler
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    
# Create your views here.
def post(self,request):
    file_model = Events()
    _, file = request.FILES.popitem()
    file = file[0]
    file_model.file = file
    file_model.save()

    #return HttpResponse(content_type='text/plain', content='Event added')




@api_view(['GET','POST'])
def events_list(request):
    if request.method == 'GET':
        events = Events.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            events = events.filter(name_icontains=name)

        events_serializer = EventsSerializer(events, many=true)
        return JsonResponse(events_serializer.data, safe=False)
        #safe=false for object serialization

    elif request.method == 'POST':
            events_data = JSONParser().parse(request)
            events_serializer = EventsSerializer(data=events_data)
            if events_serializer.is_valid():
                events_serializer.save()
                return JsonResponse(events_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(events_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def events_details(request, pk):
    try:
        events = Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return JsonResponse({'message': 'The Event does not exist'},status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        events_serializer = EventsSerializers(register)
        return JsonResponse(events_serializer.data)
    
    elif request.method == "PUT":
        events_data = JSONParser().parse(request)
        events_serializer = EventsSerializer(events, data=events_data)
        if events_serializer.is_valid():
                events_serializer.save()
                return JsonResponse(events_serializer.data)
                return JsonResponse(events_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        events.delete()
        return JsonResponse({'message': 'Event was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
