from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import pandas as pd

from rest_framework.parsers import MultiPartParser



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, EventSerializer
from .models import User, Event
import jwt, datetime
# from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def index(request):
    return HttpResponse("Welcome to FlyFlights APP!")

# @method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    def post(self,request):
        print(30*'=')
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)

class RegisterFromCSVView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.data['file']
        data = pd.read_csv(file)
        print(30*'=')
        print(data)

        for _, row in data.iterrows():
            user = User(
                email=row['email'],
                password=row['password'],
            )
            user.save()

        return Response('Users created successfully.')

class CreateEventView(APIView):
    def post(self,request):
        print(30*'=')
        print(request.data)
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)

class DeleteEventView(APIView):
    def delete(self, request, event_id):
        token = request.COOKIES.get('jwt')
        print(request.COOKIES)

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id = payload['id']).first()
        event = get_object_or_404(Event, pk=event_id)
        print(10*'=')
        # print(f'user: {user}')

        # if user != event.created_by:
        #     raise AuthenticationFailed('Unauthorized!')

        event.delete()

        return Response({'message': 'Event deleted successfully!'})

# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() +  datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow() }
        token = jwt.encode(payload, 'SECRET', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt':token}
        print(f"\\n\n\n\n{response.data}")
        return response

# @method_decorator(csrf_exempt, name='dispatch')
class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(request.COOKIES)

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
        # return Response(request.data)

class isAuthenticated(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(request.COOKIES)

        if not token:
            return JsonResponse({'isAuthenticated': False})

        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            return JsonResponse({'isAuthenticated': False})

        return JsonResponse({'isAuthenticated': True})

class EventView(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

# @method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):

    def get(self, reuquest):


        response = Response()
        response.delete_cookie('jwt')
        response.data ={'message': 'success'}


        return response