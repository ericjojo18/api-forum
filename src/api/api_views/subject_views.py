from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from api.serializers.subject_serializer import SujetSerializer
from api.models.subject_model import SujetModel

@csrf_exempt
def sujet_list(request):
    if request.method == 'GET':
        users = SujetModel.objects.all()
        serializer = SujetSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SujetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def sujet_details(request, pk):
    try:
        user = SujetModel.objects.get(pk=pk)
    except SujetModel.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = SujetSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SujetSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)