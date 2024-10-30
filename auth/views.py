from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    
    return Response({})

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        
    return Response({})

@api_view(['POST'])
def profile(request):
    return Response({})
