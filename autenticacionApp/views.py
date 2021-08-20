from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

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

from django.views.generic.edit import CreateView
from autenticacionApp.models import restauranteUser
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from autenticacionApp.forms import Signupform

class UserCreateView(CreateView):
    model = restauranteUser
    form_class = Signupform
    template_name = 'restauranteuser_create_form.html'
    success_url = reverse_lazy('login')

from django.views.generic.edit import UpdateView
from autenticacionApp.forms import Updateform

class UserUpdateView(UpdateView):
    model = restauranteUser
    form_class = Updateform
    template_name = 'restauranteuser_update_form.html'
    success_url = reverse_lazy('login')