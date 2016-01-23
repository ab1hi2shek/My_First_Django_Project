from django import forms

from .models import SignUp


class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')

		if not domain =='gmail':
			raise forms.ValidationError("Please Enter A Valid Gmail Address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#if len(full_name)<=2:
		#	raise forms.ValidationError("At Least 3 characters")
		return full_name