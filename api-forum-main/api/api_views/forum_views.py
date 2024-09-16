from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from api.serializers.forum_serializer import ForumSerializer
from api.models.forum_model import ForumModel

@csrf_exempt
def forum_list(request):
    if request.method == 'GET':
        users = ForumModel.objects.all()
        serializer = ForumSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ForumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def forum_details(request, pk):
    try:
        user = ForumModel.objects.get(pk=pk)
    except ForumModel.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = ForumSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ForumSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)