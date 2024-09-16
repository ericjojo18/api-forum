from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from api.serializers.message_serializer import MessageSerializer
from api.models.message_model import MessageModel

@csrf_exempt
def message_list(request):
    if request.method == 'GET':
        users = MessageModel.objects.all()
        serializer = MessageSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def message_details(request, pk):
    try:
        user = MessageModel.objects.get(pk=pk)
    except MessageModel.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = MessageSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)