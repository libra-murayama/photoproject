# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = ('username', 'email', 'password1', 'password2')