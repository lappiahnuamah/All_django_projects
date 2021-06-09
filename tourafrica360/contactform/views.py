from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        comment = request.POST.get('comment')

        data = {
            'name': name,
            'email':email,
            'subject':subject,
            'comment':comment
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['comment'], data['email'])
        send_mail(data['subject'], message, '', ['techinnovahub@gmail.com'])

    return render(request, 'contact.html',{})