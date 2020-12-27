from django import forms  
from .models import User_Resistrations

class UserResistrationForm(forms.ModelForm):  
    class Meta:  
        model = User_Resistrations  
        fields = ['fname','lname','email','u_password']
        widgets = {'fname':forms.TextInput(attrs={'class':'form-control'}),
                    'lname':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.TextInput(attrs={'class':'form-control'}),
                    'u_password':forms.PasswordInput(attrs={'class':'form-control'}),
                
                    }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User_Resistrations  
        fields = ['email','u_password']
        widgets = {'email':forms.TextInput(attrs={'class':'input100','placeholder':'Email'}),
                    'u_password':forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'}) }




# from django import forms  
# from .models import User_Resistrations

# class UserResistrationForm(forms.ModelForm):  
#     class Meta:  
#         model = User_Resistrations  
#         fields = "__all__" 