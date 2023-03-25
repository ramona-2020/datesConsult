from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from datesConsult.app_auth.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'