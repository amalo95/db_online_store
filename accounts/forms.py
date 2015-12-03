from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError("Invalid Password")
		elif user is None:
			pass
		else:
			return password

  	#def clean_password2(self):
		# password1 = self.cleaned_data.get('password1')
		# password2 = self.cleaned_data.get('password2')
		# if password1 and password2 and password1 != password2:
		# 	raise forms.ValidationError("Passwords do not match")
		# return password2

	

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address',)


# class RegistrationForm(forms.ModelForm):
# 	password1 = forms.CharField(label='Password', \
# 					widget=forms.PasswordInput())
# 	password2 = forms.CharField(label='Password Confirmation', \
# 					widget=forms.PasswordInput())

# 	class Meta:
# 		model = UserProfile
# 		fields = ['first_name', 'last_name', 'email', 'name', 'address', 'username']

# 	def clean_password2(self):
# 		password1 = self.cleaned_data.get('password1')
# 		password2 = self.cleaned_data.get('password2')
# 		if password1 and password2 and password1 != password2:
# 			raise forms.ValidationError("Passwords do not match")
# 		return password2

# 	def clean_email(self):
# 		email = self.cleaned_data.get("email")
# 		user_count = User.objects.filter(email=email).count()
# 		if user_count > 0:
# 			raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
# 		return email


# 	def save(self, commit=True):
# 		user = super(RegistrationForm, self).save(commit=False)
# 		user.set_password(self.cleaned_data['password1']) 
# 		if commit:
# 			user.save()
# 		return user