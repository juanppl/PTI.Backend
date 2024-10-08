
# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status

from PTIBackend.serializers import RegisterUserSerializer, UpdateUserSerializer, UserSerializer

from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username,
            'is_superuser': user.is_superuser,
            'user_permissions':  list(user.user_permissions.values_list('codename', flat=True))
        })
    

@api_view(['POST'])
@permission_classes([AllowAny])
def create_auth(request):
    serialized = RegisterUserSerializer(data=request.data)
    if serialized.is_valid():
        user = User(
            email=serialized.validated_data['email'],
            username=serialized.validated_data['username']
        )
        user.set_password(serialized.validated_data['password'])
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


