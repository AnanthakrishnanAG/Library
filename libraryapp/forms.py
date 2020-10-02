from django import forms
class SignUp(forms.Form):

    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Name'}),error_messages={'required':'please enter a name'})
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','type':'password'}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'ConfirmPassword','type':'password'}))

    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    

    def passwordLength(self):
        if len(self.cleaned_data.get('password')) <4 :
            raise forms.ValidationError('Password should have atleast 4 charactors')
        else:
            return True



class LoginForm(forms.Form):
    email= forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','type':'password'}))