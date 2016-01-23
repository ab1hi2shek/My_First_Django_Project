from django.shortcuts import render

from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request): 
	title = 'Welcome Guest'
	new = "thanks for visiting our Website"
	# if request.user.is_authenticated():
	# 	title = "Welcome %s" %(request.user)
	# 	new = "Glad to see you again"

	#add a form
	form = SignUpForm(request.POST or None)

	context = {
		"title":title,
		"new":new,
		"form":form,
	}



	if form.is_valid():
		#form.save() it saves the form instantly

		#print request.POST['email'] #not recommended as it skips all validators and grab raw data
		instance = form.save(commit=False) #it skips the instant saving and we can do stuffs in mean time
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Anonymous"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = 'Anonymous'
		instance.save()
		print instance.email
		print instance.timestamp
		context = {
		"title":"Thank you",
		"new":full_name,
		#"form":form,
	}

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key, value in form.cleaned_data.iteritems():
			print key,value
			#print form.cleaned_data.get(key)
		#email = form.cleaned_data.get("email")
		#message = form.cleaned_data.get("message")
		#full_name = form.cleaned_data.get("full_name")

	context = {
		"form": form,
	}
	return render(request, "forms.html", context)

