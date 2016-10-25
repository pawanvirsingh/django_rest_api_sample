from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tomcarapi.models import tomcarapi
from tomcarapi.serializers import tomcarapiSerializer





class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)




@api_view(['GET', 'POST'])
def tomcarapi_list(request):
    """
    List all tomcarapis, or create a new tomcarapi.
    """
    if request.method == 'GET':
        tomcarapis = tomcarapi.objects.all()
        serializer = tomcarapiSerializer(tomcarapis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = tomcarapiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tomcarapi_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = tomcarapi.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = tomcarapiSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = tomcarapiSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tomcarapi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


