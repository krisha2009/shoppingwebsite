from .models import User

class Myform(forms.ModelForm):
    class Meta:
        model=User
        fields=["email","contact","uname","password,"]
        labels={"email":"Email","contact":"MobileNo","uname":"Username","paswword":"Password",}