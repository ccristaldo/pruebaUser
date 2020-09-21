from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
	class Meta:
		model = Usuario
		fields = ['username',
				'first_name',
				'last_name',				
				'password1',
				'password2',]
		exclude = ['email',
				'provincia',
				'ciudad',
				'universidad',
				'carrera']
		help_texts = {
				'username': None,
				'password1': None,
				'password2': None,
			}

class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['email',
				'provincia',
				'ciudad',
				'universidad',
				'carrera']