from rest_framework import  status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.emails.emails import businessemailcreation
from rest_framework.decorators import api_view, permission_classes
from business.models import Business
from profiles.models import Profile
from business.api.serializers import BusinessSerializer,BusinessUpdateSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from accounts.models import Account

from django.db.models import Q

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_business(request, name=None):
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
        
        if name:
            businesses = Business.objects.filter(Q(name__iexact=name) & Q(owner=profile))
        else:
            businesses = Business.objects.filter(owner=profile)
        
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)
    except Business.DoesNotExist:
        return Response({'detail': 'No registered businesses.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_business(request, name):
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
        business = get_object_or_404(Business, name=name, owner=profile)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)
    except Business.DoesNotExist:
        return Response({'detail': 'Business not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_business(request):
    parser_classes = [MultiPartParser, FormParser]
    serializer = BusinessSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        account=Account.objects.filter(id=user.id)
        account.update(is_merchant=True)
        profile = Profile.objects.get(user=user.id)        
        serializer.save(owner=profile)
        return Response({'detail': 'Business registered successfully check your email to verify  your Business'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_business(request, name):
    parser_classes = [MultiPartParser, FormParser]
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
        business = Business.objects.get(owner=profile, name=name)
    except Business.DoesNotExist:
        return Response({'detail': 'Business not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BusinessUpdateSerializer(business, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Updated successfully.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_business_admin(request, name=None):
    try:        
        businesses = Business.objects.all()
        
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)
    except Business.DoesNotExist:
        return Response({'detail': 'No registered businesses.'}, status=status.HTTP_404_NOT_FOUND)