from django import forms
from .models import Blog_Users

class Create_UserForm(forms.ModelForm):
	username = forms.CharField(max_length = 35)
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput(attrs={'class':"ml-1","name":"c_password"}))
	
	class Meta:
		model = Blog_Users
		fields =['username','password']
	
	def clean_username(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		query_set = Blog_Users.objects.filter(username = username)
		if " " in username:
			raise forms.ValidationError("There cannot be whitespace between your username")
		elif query_set.exists():
			raise forms.ValidationError("Username already Exists!")
		return username 


class Login_UserForm(forms.Form):
	username = forms.CharField(max_length = 35,widget = forms.TextInput(attrs={}))
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput(attrs={'class':"ml-1","name":"l_password"}))

	def clean_username(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		query_set = Blog_Users.objects.filter(username = username, password = password)
		if " " in username:
			raise forms.ValidationError("There cannot be whitespace between your username")
		'''elif query_set.exists():
			raise forms.ValidationError("Account  Exist")
		else:
			raise forms.ValidationError("Account Doesn,t Exist\nCreate an Account first")'''
		return username 
