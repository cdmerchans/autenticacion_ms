from autenticacionApp.models import restauranteUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class Signupform(UserCreationForm):

    class Meta:
        model = restauranteUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'phone_number']
        labels = {
            'username': 'Nombre de usuario', 
            'email': 'Correo electrónico', 
            'first_name': 'Nombres', 
            'last_name': 'Apellidos', 
            'phone_number': 'Teléfono'
            }
            
class Updateform(UserChangeForm):

    class Meta:
        model = restauranteUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'phone_number']
        labels = {
            'username': 'Nombre de usuario', 
            'email': 'Correo electrónico', 
            'first_name': 'Nombres', 
            'last_name': 'Apellidos', 
            'phone_number': 'Teléfono'
            }            