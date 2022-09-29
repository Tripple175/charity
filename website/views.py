from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html', {})
def blog(request):
	return render(request, 'blog.html', {})
def about(request):
	return render(request, 'about.html', {})
def causes(request):
	return render(request, 'causes.html', {})
def contact(request):
	if request.method == "POST":
		m_firstname = request.POST['firstname']
		m_lastname = request.POST['lastname']
		m_email = request.POST['email']
		message = request.POST['message']


		#send an email
		send_mail(
			'message from' + m_firstname, #subject
			message,#message
			m_email,#from email
			['hptripple@gmail.com',	'tripple.hope@yahoo.com'],#to email
			)


		return render(request, 'contact.html', {'m_firstname':m_firstname})

	else:
		return render(request, 'contact.html', {})
