from django import forms

class takeInput(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    device_ip = forms.CharField(label="Device IP", widget=forms.TextInput(attrs={'placeholder': 'Device IP', 'class': 'form-control'}))
    self_ip = forms.CharField(label="Enter the BGP self IP", widget=forms.TextInput(attrs={'placeholder': 'BGP self IP', 'class': 'form-control'}))
    peer_ip = forms.CharField(label="Enter the BGP peer IP", widget=forms.TextInput(attrs={'placeholder': 'BGP peer IP', 'class': 'form-control'}))
    self_AS = forms.IntegerField(label="Enter self AS number", widget=forms.TextInput(attrs={'placeholder': 'Self AS number', 'class': 'form-control'}))
    remote_AS = forms.IntegerField(label="Enter remote AS number", widget=forms.TextInput(attrs={'placeholder': 'Remote AS number', 'class': 'form-control'}))
    device_select = forms.ChoiceField(label="Enter IOS or XE", choices=(("IOS","IOS"), ("XE","XE")), widget=forms.Select(attrs={'class': 'form-control'}))