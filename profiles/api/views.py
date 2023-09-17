from rest_framework import generics, status
from rest_framework.response import Response
from profiles.api.serializers import ProfileSerializer
from accounts.emails.emails import profilecompleteemail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from rest_framework.exceptions import PermissionDenied, ValidationError

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise PermissionDenied('Profile not found')

    if request.method == 'POST':
        data = request.data.copy()  # Make a copy of the request data

        # Check if both first name and last name are present in the request data
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if first_name and last_name:
            # If both first name and last name are filled, set verified to True
            data['verified'] = True

        serializer = ProfileSerializer(instance=profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise ValidationError(serializer.errors)

    return Response({'detail': 'Invalid request method'}, status=405)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_check_view(request):
    try:
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({'detail': 'create profile.'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_check_verified_view(request):
    try:
        user = request.user
        profile = Profile.objects.filter(user=user, verified=True)

        if profile.exists():
            return Response({'detail': 'Profile is verified'},status=200)
        
    except Profile.DoesNotExist:
        return Response({'error':'Profile does not exist or is not verified' },status=400)


