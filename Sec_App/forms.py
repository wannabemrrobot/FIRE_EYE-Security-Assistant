from django import forms
from .functions import check

class getIp(forms.Form):

    ip      = forms.CharField(max_length=15,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'                    Enter a Valid IP Address '
                                }))

    def clean_ip(self):
        ip = self.cleaned_data.get('ip')
        if check(ip)==0:
            raise forms.ValidationError("Enter a Valid IP Address")
        return ip

class getUrl(forms.Form):

    url      = forms.CharField(widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter a Valid URL of a Web Application '
                                }))

