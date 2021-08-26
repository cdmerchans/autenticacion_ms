from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from autenticacionApp.models import restauranteUser
from django.urls import reverse_lazy

from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import re

class VerifyTokenView(TokenVerifyView):

    def post(self, request, *args, **kwargs):
        token = request.data['token']
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            valid_data = tokenBackend.decode(token,verify=False)
            serializer.validated_data['UserId'] = valid_data['user_id']
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class CrearUsuario(APIView):

    def post(self, request, *args, **kwargs):

        username = request.data['username']
        password = make_password(request.data['password'])
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        address = request.data['address']
        phone_number = request.data['phone_number']

        usuario = restauranteUser.objects.filter(username = username)

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        bandera_email = re.fullmatch(regex, email)
        badera_phone_number = phone_number.isnumeric()

        if bandera_email and badera_phone_number:

            if not usuario:

                new_usuario = restauranteUser(username = username, email = email, first_name = first_name, last_name = last_name, address = address, phone_number = phone_number, password = password)
                new_usuario.save()

                return Response({"mensaje": "Usuario creado"}, status=status.HTTP_201_CREATED)

            else:
            
                return Response({"mensaje": "Ya hay un usuario con ese username"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:

            if not bandera_email:

                return Response({"mensaje": "El email no es válido"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            elif not badera_phone_number:

                return Response({"mensaje": "El telefono no es válido"}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ConsultarUsuario(APIView):

    def get(self, request, *args, **kwargs):

        username = request.query_params.get('username', None)

        if username is None:

            return Response({"mensaje": "El username está vacio"},status=status.HTTP_404_NOT_FOUND)

        else:

            usuario = restauranteUser.objects.filter(username = username).values('id', 'username', 'email', 'first_name', 'last_name', 'address', 'phone_number')

            if not usuario:

                return Response({"mensaje": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            else:
    
                usuario = list(usuario)

                return JsonResponse(usuario, safe=False, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):

        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        address = request.data['address']
        phone_number = request.data['phone_number']

        usuario = restauranteUser.objects.filter(username = username)


        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        bandera_email = re.fullmatch(regex, email)
        badera_phone_number = phone_number.isnumeric()

        if bandera_email and badera_phone_number:
            
            if not usuario:

                return Response({"mensaje": "No hay usuario que actualizar"}, status=status.HTTP_404_NOT_FOUND)

            else:

                restauranteUser.objects.filter(username = username).update(email= email, first_name= first_name, last_name= last_name, address=  address, phone_number = phone_number)
            
                return Response({"mensaje": "El usuario fue actualizado"}, status=status.HTTP_200_OK)
        else:

            if not bandera_email:

                return Response({"mensaje": "El email no es válido"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            elif not badera_phone_number:

                return Response({"mensaje": "El telefono no es válido"}, status=status.HTTP_406_NOT_ACCEPTABLE)

class BuscarUsuario(APIView):

    def get(self,request, pk):

        usuario = restauranteUser.objects.filter(pk=pk).values('id', 'username', 'email', 'first_name', 'last_name', 'address', 'phone_number')

        if not usuario:

            return Response({"mensaje": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        else:
  
            usuario = list(usuario)

            return JsonResponse(usuario, safe=False, status=status.HTTP_200_OK)