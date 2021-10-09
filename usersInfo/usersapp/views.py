from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import UserAccount
from rest_framework.pagination import PageNumberPagination

@permission_classes([AllowAny,])
@api_view(['GET', 'POST','PUT',"DELETE"])
def UserInfo(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        data=UserAccount.objects.all()
        result_page = paginator.paginate_queryset(data, request)
        ser=UserSerializer(result_page,many=True)
        return JsonResponse(ser.data,safe=False,status=200)

    if request.method == 'PUT':
        try:
            username=request.data.get("username")
            snippet = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            return JsonResponse({"message":"user data not found."},status=400)

        sers=UserSerializer(snippet,request.data)
        if sers.is_valid():
            sers.save()
            return JsonResponse({"message": username + " data is updated in database."},status=200)

        return JsonResponse(sers.errors,safe=False,status=200)

    if request.method == 'POST':
        data=JSONParser().parse(request)
        sers=UserSerializer(data=data)
        if sers.is_valid():
            sers.save()
            return JsonResponse({"message": "Data saved to database"},status=200)
        return JsonResponse(sers.errors,status=400)


    if request.method == 'DELETE':
        try:
            username=request.data.get("username")
            snippet = UserAccount.objects.get(username=username)
            snippet.delete()
            return JsonResponse({"message":username + " data has been deleted."},status=400)

        except UserAccount.DoesNotExist:
            return JsonResponse({"message":"user data not found."},status=400)
