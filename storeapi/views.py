from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from store.models import medicine
from .serializer import medicineserializer, searchsealizer
from django.contrib.auth.models import User
from django.db.models import Q


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    use = request.data.get("username")
    pas = request.data.get("password")
    if use is None or pas is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(username=use, password=pas)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    use = request.data.get("username")
    email = request.data.get("email")
    pas = request.data.get("password")
    pas2 = request.data.get("password2")
    if pas != pas2:
        return Response({'error': 'the confirmation password is wrong'})
    user = User.objects.create_user(use, email, pas)
    user.save()
    return Response({'done': 'user creation done'}, status=HTTP_200_OK)


@api_view(["GET"])
def medicinedetail(request):
    val = medicine.objects.all()
    serializer = medicineserializer(val, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def search(request):
    result = []
    query = request.data.get("search")
    result = medicine.objects.filter(Q(title__icontains=query))
    serializer = searchsealizer(result, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def logoutt(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')

@api_view(["DELETE"])
def delete(request):
    pk=request.data.get("pk")
    item = get_object_or_404(medicine, pk=pk)
    item.delete()
    return Response("deleted")
@api_view(["POST"])
def create(request):
    med=medicineserializer(data=request.data)
    if med.is_valid():
        med.save()
        return Response(med.data)
@api_view(["PUT"])
def update(request):
    pk=request.data.get("pk")
    item = get_object_or_404(medicine, pk=pk)
    item.title=request.data.get("title")
    item.price=request.data.get("price")
    item.status=request.data.get("status")
    item.no_of_pack=request.data.get("no_of_pack")
    item.exp=request.data.get("exp")
    item.save()
    return Response("updated")
